# Standard Library
from unittest import mock, TestCase

# Apps
from recipe.service.recipe_service import RecipeService
from recipe.dto.recipe import RecipeDto


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
        RecipeDto(id=2, name="Asado", description="Best dish in the world", ingredients=[]),
    ]


class TestRecipeService(TestCase):
    @mock.patch("recipe.repository.recipe_repository.RecipeRepository.get_all")
    def test_get_all_recipes_from_db(self, mock_repository):
        dtos = create_dtos()
        mock_repository.return_value = dtos

        res = RecipeService.get_recipes()

        mock_repository.assert_called_once()
        assert res == dtos
