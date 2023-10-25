# Standard Library
from unittest import mock, TestCase

# Apps
from recipe.api.recipe_api import RecipeAPI
from recipe.dto.recipe import RecipeDto


def create_dtos():
    return [
        RecipeDto(
            id=1, name="Milanesa", description="Great dish, always served with potatoes"
        ),
        RecipeDto(id=2, name="Asado", description="Best dish in the world"),
    ]


class TestRecipeAPI(TestCase):
    @mock.patch("recipe.repository.recipe_repository.RecipeRepository.get_all")
    def test_get_all_recipes_from_db(self, mock_repository):
        dtos = create_dtos()
        mock_repository.return_value = dtos

        res = RecipeAPI.get_recipes()

        mock_repository.assert_called_once()
        assert res == dtos
