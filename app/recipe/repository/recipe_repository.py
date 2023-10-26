# Dependencies
from typing import List

# From apps
from recipe.dto.recipe import RecipeDto
from core.models import Recipe


class RecipeRepository:
    @staticmethod
    def get_all() -> List[RecipeDto]:
        recipes_with_ingredients = list(Recipe.objects.prefetch_related("ingredients").all().order_by("-name"))
        return [RecipeDto.model_validate(recipe) for recipe in recipes_with_ingredients]

