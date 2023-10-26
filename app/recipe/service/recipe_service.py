# Dependencies
from typing import List

# From apps
from recipe.repository.recipe_repository import RecipeRepository
from recipe.dto.recipe import RecipeDto


class RecipeService:
    @staticmethod
    def get_recipes() -> List[RecipeDto]:
        return RecipeRepository.get_all()
