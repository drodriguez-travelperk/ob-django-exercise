"""
Tests for database models
"""
from django.test import TestCase

from core import models


class ModelTests(TestCase):
    """Test models"""

    def test_create_recipe(self):
        """Create a single recipe and test the string representation"""
        recipe = models.Recipe.objects.create(
            name="Barbecue", description="Best food in the world."
        )

        self.assertEqual(str(recipe), recipe.name)

    def test_create_recipe_with_ingredient(self):
        """Create a recipe with some ingredients and test the string representation"""
        recipe = models.Recipe.objects.create(
            name="Breaded steak",
            description="Nothing can describe the taste of this plate, you have to try it.",
        )
        ingredient = models.Ingredient.objects.create(name="steak", recipe=recipe)

        self.assertEqual(str(ingredient), ingredient.name)
