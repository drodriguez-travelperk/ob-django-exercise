# Dependencies
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework import status

# From apps
from recipe.service.recipe_service import RecipeService


class RecipeViewSet(ViewSet):
    """View for manage recipe apis"""

    @staticmethod
    def list(request: Request) -> Response:
        """Get and return the list of recipes"""
        res = RecipeService.get_recipes()
        recipes = [recipe_dto.model_dump() for recipe_dto in res]

        return Response(data=recipes, status=status.HTTP_200_OK)
