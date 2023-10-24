"""
Serializer for Recipe API
"""
from rest_framework import serializers

from core.models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """Ingredient Serializer"""

    class Meta:
        model = Ingredient
        fields = ['name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    """Recipe Serializer"""
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'ingredients']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a recipe with ingredients"""
        ingredients = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        if ingredients:
            for ingredient in ingredients:
                Ingredient.objects.create(recipe=recipe, **ingredient)

        return recipe

    def update(self, instance, validated_data):
        """Update a recipe overwriting all ingredients"""
        ingredients = validated_data.pop('ingredients', [])
        if ingredients:
            instance.ingredients.all().delete()  # Delete old recipe ingredients.
            for ingredient in ingredients:
                Ingredient.objects.create(recipe=instance, **ingredient)

        super().update(instance, validated_data)
        return instance


