# Standard Library
from unittest import mock, TestCase

# Apps
from recipe.service.recipe_service import RecipeService
from recipe.dto.recipe import RecipeDto, IngredientDto

# Dependencies
from django.core.exceptions import ObjectDoesNotExist

# Apps
from core.models import Recipe, Ingredient


class TestRecipeService(TestCase):
    def test_create_recipe(self):
        payload = {
            "name": "Milanesa",
            "description": "Best dish in the world",
            "ingredients": []
        }
        res = RecipeService.create(**payload)
        self.assertIsInstance(res, RecipeDto)

        expected = RecipeDto(**payload, id=res.id)
        self.assertEqual(res, expected)
        RecipeService.delete_recipe(res.id)

    def test_get_all_recipes_from_db(self):
        recipe_1_payload = {
            "name": "Recipe 1",
            "description": "fancy description",
            "ingredients": [{"name": "garlic"}]
        }
        recipe_2_payload = {
            "name": "Recipe 2",
            "description": "description for recipe 2",
            "ingredients": [{"name": "tomato"}]
        }

        RecipeService.create(**recipe_1_payload)
        RecipeService.create(**recipe_2_payload)

        res = RecipeService.get_all()
        self.assertEqual(len(res), 2)

    def test_get_recipe_from_db(self):
        recipe_payload = {
            "name": "Pizza",
            "description": "From Italy",
            "ingredients": [{"name": "cheese"}]
        }

        recipe = RecipeService.create(**recipe_payload)

        res = RecipeService.get_by_id(recipe.id)
        self.assertIsInstance(res, RecipeDto)
        self.assertIsInstance(res.ingredients[0], IngredientDto)

    def test_get_recipe_from_db_not_found(self):
        with self.assertRaises(ObjectDoesNotExist):
            RecipeService.get_by_id(422)

    def test_delete_recipe_success(self):
        recipe = RecipeService.create(**{
            "name": "Pizza",
            "description": "From Italy",
            "ingredients": [{"name": "tomato"}]
        })

        RecipeService.delete_recipe(recipe.id)

        recipe_on_db = Recipe.objects.filter(pk=recipe.id).exists()
        self.assertFalse(recipe_on_db)

    def test_delete_recipe_raise_not_exist(self):
        with self.assertRaises(ObjectDoesNotExist):
            RecipeService.delete_recipe(123)
