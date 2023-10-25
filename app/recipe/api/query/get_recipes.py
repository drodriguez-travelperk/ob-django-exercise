# Dependencies
from typing import List

# From apps
from recipe.dto.recipe import RecipeDto
from recipe.repository.recipe_repository import RecipeRepository


class QueryRecipeAPI:
    @staticmethod
    def get_recipes() -> List[RecipeDto]:
        return RecipeRepository.get_all()
