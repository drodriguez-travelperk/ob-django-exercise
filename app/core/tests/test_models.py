"""
Tests for database models
"""
from django.test import TestCase

from core import models


class ModelTests(TestCase):
    """Test models"""

    def test_create_recipe(self):
        recipe = models.Recipe.objects.create(
            name="Barbecue",
            description="Best food in the world."
        )

        self.assertEqual(str(recipe), recipe.name)
