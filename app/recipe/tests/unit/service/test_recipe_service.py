# Standard Library
from unittest import mock, TestCase

# Apps
from recipe.service.recipe_service import RecipeService
from recipe.dto.recipe import RecipeDto

# Dependencies
from django.core.exceptions import ObjectDoesNotExist

# Apps
from core.models import Recipe, Ingredient

def create_dtos():
    return [
        RecipeDto(
            id=1,
            name="Milanesa",
            description="Great dish, always served with potatoes",
            ingredients=[
                {"id": 1, "name": "garlic"},
                {"id": 2, "name": "bread crumb"},
                {"id": 3, "name": "steak"}
            ]
        ),
        RecipeDto(id=2, name="Asado", description="There are no words to describe it. You have to try it", ingredients=[]),
    ]


class TestRecipeService(TestCase):
    @mock.patch("recipe.repository.recipe_repository.RecipeRepository.get_all")
    def test_get_all_recipes_from_db(self, mock_repository):
        dtos = create_dtos()
        mock_repository.return_value = dtos

        res = RecipeService.get_recipes()

        mock_repository.assert_called_once()
        self.assertEqual(res, dtos)

    @mock.patch("recipe.repository.recipe_repository.RecipeRepository.get_by_id")
    def test_get_recipe_from_db(self, mock_repository):
        dto = create_dtos()[0]
        mock_repository.return_value = dto

        res = RecipeService.get_recipe_by_id(1)

        mock_repository.assert_called_once_with(1)
        self.assertEqual(res, dto)

    @mock.patch("recipe.repository.recipe_repository.RecipeRepository.get_by_id")
    def test_get_recipe_from_db_not_found(self, mock_repository):
        mock_repository.return_value = None

        res = RecipeService.get_recipe_by_id(1)

        mock_repository.assert_called_once_with(1)
        self.assertIsNone(res)

    @mock.patch("recipe.repository.recipe_repository.RecipeRepository.create")
    def test_create_recipe(self, mock_repository):
        payload = {
            "name": "Milanesa",
            "description": "Best dish in the world",
            "ingredients": []
        }
        RecipeService.create(**payload)
        mock_repository.assert_called_once_with(**payload)

    def test_delete_recipe_success(self):
        recipe = Recipe.objects.create(name="Pizza", description="From Italy")
        Ingredient.objects.create(recipe=recipe, name="Tomato")

        RecipeService.delete_recipe(recipe.id)

        recipe_on_db = Recipe.objects.filter(pk=recipe.id).exists()
        self.assertFalse(recipe_on_db)

    def test_delete_recipe_raise_not_exist(self):
        with self.assertRaises(ObjectDoesNotExist):
            RecipeService.delete_recipe(123)
