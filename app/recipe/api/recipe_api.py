# From apps
from typing import List

from recipe.dto.recipe import RecipeDto
from recipe.api.query.get_recipes import QueryRecipeAPI


class RecipeAPI:
    @staticmethod
    def get_recipes() -> List[RecipeDto]:
        """Get all recipes"""
        return QueryRecipeAPI.get_recipes()
