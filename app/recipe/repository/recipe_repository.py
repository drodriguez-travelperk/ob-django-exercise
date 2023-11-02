# Dependencies
from typing import List, Optional
from django.core.exceptions import ObjectDoesNotExist

# From apps
from recipe.dto.recipe import RecipeDto
from core.models import Recipe, Ingredient
from recipe.schema.create_recipe_schema import CreateRecipeRequestSchema


class RecipeRepository:
    @staticmethod
    def create(**payload: CreateRecipeRequestSchema) -> RecipeDto:
        ingredients = payload.pop("ingredients", [])
        recipe = Recipe.objects.create(**payload)
        if ingredients:
            for ingredient in ingredients:
                Ingredient.objects.create(recipe=recipe, **ingredient)
        return RecipeDto.model_validate(recipe)

    @staticmethod
    def get_all() -> List[RecipeDto]:
        recipes_with_ingredients = list(Recipe.objects.prefetch_related("ingredients").all().order_by("-name"))
        return [RecipeDto.model_validate(recipe) for recipe in recipes_with_ingredients]

    @staticmethod
    def get_by_id(recipe_id: int) -> Optional[RecipeDto]:
        try:
            recipe = Recipe.objects.prefetch_related("ingredients").get(pk=recipe_id)
            recipe_dto = RecipeDto.model_validate(recipe)
            return recipe_dto
        except Recipe.DoesNotExist:
            raise ObjectDoesNotExist

    @staticmethod
    def delete(recipe_id: int) -> None:
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
            recipe.delete()
        except Recipe.DoesNotExist:
            raise ObjectDoesNotExist


