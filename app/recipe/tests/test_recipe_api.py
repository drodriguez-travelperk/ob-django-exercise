"""
Tests for Recipe API
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer

RECIPES_URL = reverse('recipe:recipe-list')


class RecipeAPITests(TestCase):
    """Test Recipe API"""

    def setUp(self):
        client = APIClient()

    def test_retrieve_recipes(self):
        """Retrieve a list of recipes"""
        Recipe.objects.create(
            name="Barbecue",
            description="Argentinean food. There are no words to describe it."
        )
        Recipe.objects.create(
            name="Noodles",
            description="Homemade pasta, grandma's recipe."
        )

        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.all().order_by('-name')
        serialized = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serialized.data)
