# Dependencies
import jsonref
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework import status
from pydantic import ValidationError
from drf_yasg.openapi import Schema
from drf_yasg.utils import swagger_auto_schema

# From apps
from recipe.service.recipe_service import RecipeService
from recipe.schema.create_recipe_schema import CreateRecipeRequestSchema, CreateRecipeResponseSchema


class RecipeViewSet(ViewSet):
    """View for manage recipe apis"""
    @staticmethod
    @swagger_auto_schema(
        request_body=Schema(**jsonref.replace_refs(CreateRecipeRequestSchema.model_json_schema()))
    )
    def create(request: Request) -> Response:
        try:
            validated_data = CreateRecipeRequestSchema.model_validate(request.data)
            res = RecipeService.create(**validated_data.model_dump())
            return Response(status=status.HTTP_201_CREATED, data=res.model_dump())
        except ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def list(request: Request) -> Response:
        """Get and return the list of recipes"""
        res = RecipeService.get_recipes()
        recipes = [recipe_dto.to_json() for recipe_dto in res]

        return Response(data=recipes, status=status.HTTP_200_OK)

    @staticmethod
    def retrieve(request: Request, pk=None) -> Response:
        res = RecipeService.get_recipe_by_id(pk).to_json()
        return Response(data=res, status=status.HTTP_200_OK)

