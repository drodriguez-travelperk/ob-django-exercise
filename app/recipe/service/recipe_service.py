# Dependencies
from typing import List

# From apps
from recipe.repository.recipe_repository import RecipeRepository
from recipe.dto.recipe import RecipeDto


class RecipeService:
    @staticmethod
    def get_recipes() -> List[RecipeDto]:
        return RecipeRepository.get_all()

    @staticmethod
    def get_recipe_by_id(id: int) -> RecipeDto:
        return RecipeRepository.get_by_id(id)
