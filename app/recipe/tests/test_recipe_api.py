"""
Tests for Recipe API
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe, Ingredient

from recipe.serializers import RecipeSerializer

RECIPES_URL = reverse("recipe:recipe-list")


def detail_url(recipe_id):
    """Creates and return a recipe detail url"""
    return reverse("recipe:recipe-detail", args=[recipe_id])


def create_recipe(**params):
    """Creates and return a recipe"""
    defaults = {
        "name": "Pizza",
        "description": "dish of Italian origin consisting of a flattened disk of bread dough",
    }
    defaults.update(params)

    recipe = Recipe.objects.create(**defaults)
    return recipe


class RecipeAPITests(TestCase):
    """Test Recipe API"""

    def setUp(self):
        client = APIClient()

    def test_retrieve_recipes(self):
        """Retrieve a list of recipes"""
        create_recipe(
            name="Barbecue",
            description="Argentinean food. There are no words to describe it.",
        )
        create_recipe(name="Noodles", description="Homemade pasta, grandma's recipe.")

        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.all().order_by("-name")
        serialized = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serialized.data)

    def test_update_recipe(self):
        """Test updating a recipe by id"""
        recipe = create_recipe()
        url = detail_url(recipe.id)
        payload = {"description": "updated description for the pizza recipe"}
        res = self.client.patch(url, payload, content_type="application/json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        recipe.refresh_from_db()

        self.assertEqual(recipe.description, payload["description"])

    def test_delete_recipe(self):
        """Test deleting a recipe"""
        recipe = create_recipe()
        url = detail_url(recipe.id)

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        exists_on_db = Recipe.objects.filter(id=recipe.id).exists()
        self.assertFalse(exists_on_db)

    def test_create_recipe_with_ingredients(self):
        """Test creating a recipe with ingredients"""
        payload = {
            "name": "Spanish omelette",
            "description": "traditional spanish dish",
            "ingredients": [{"name": "potato"}, {"name": "eggs"}, {"name": "onion"}],
        }

        res = self.client.post(RECIPES_URL, payload, content_type="application/json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        recipe = Recipe.objects.get(name=payload["name"])
        serialized = RecipeSerializer(recipe)
        self.assertEqual(res.data, serialized.data)

    def test_update_recipe_with_ingredients(self):
        """Test updating ingredients"""
        recipe = create_recipe(name="barbecue", description="some cool description")
        Ingredient.objects.create(recipe=recipe, name="steak")
        Ingredient.objects.create(recipe=recipe, name="chori")
        Ingredient.objects.create(recipe=recipe, name="chimi")

        self.assertEqual(recipe.ingredients.count(), 3)

        payload = {"name": "Asado!!!", "ingredients": [{"name": "vacio"}]}

        url = detail_url(recipe.id)
        res = self.client.patch(url, payload, content_type="application/json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        recipe.refresh_from_db()

        self.assertEqual(recipe.name, payload["name"])
        self.assertEqual(recipe.ingredients.count(), 1)
