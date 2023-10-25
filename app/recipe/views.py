# Dependencies
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework import status

# From apps
from recipe.api.recipe_api import RecipeAPI


class RecipeViewSet(ViewSet):
    """View for manage recipe apis"""

    @staticmethod
    def list(request: Request) -> Response:
        """Get and return the list of recipes"""
        res = RecipeAPI.get_recipes()
        recipes = [recipe_dto.dict() for recipe_dto in res]

        return Response(data=recipes, status=status.HTTP_200_OK)
