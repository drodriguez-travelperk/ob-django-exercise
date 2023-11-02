# Dependencies
from typing import List, Optional

# From apps
from recipe.schema.create_recipe_schema import CreateRecipeRequestSchema
from recipe.repository.recipe_repository import RecipeRepository
from recipe.dto.recipe import RecipeDto


class RecipeService:
    @staticmethod
    def create(**payload: CreateRecipeRequestSchema):
        return RecipeRepository.create(**payload)

    @staticmethod
    def get_all() -> List[RecipeDto]:
        return RecipeRepository.get_all()

    @staticmethod
    def get_by_id(recipe_id: int) -> Optional[RecipeDto]:
        return RecipeRepository.get_by_id(recipe_id)

    @staticmethod
    def delete_recipe(recipe_id: int) -> None:
        return RecipeRepository.delete(recipe_id)
