from recipe.schemas.recipe_schema import RecipeListResponseSchema


class RecipeAPI():
    def get_recipes(self) -> RecipeListResponseSchema:
        """Get all recipes"""
        return