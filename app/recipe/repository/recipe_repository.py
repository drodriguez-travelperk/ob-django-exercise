# From apps
from recipe.dto.recipe import RecipeDto
from core.models import Recipe


class RecipeRepository:
    @staticmethod
    def get_all():
        recipes = Recipe.objects.all().order_by("-name")
        return [RecipeDto.from_orm(recipe) for recipe in recipes]
