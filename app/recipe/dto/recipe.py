# Dependencies
from typing import List, Any

from django.db.models.manager import BaseManager
from pydantic import field_validator

# Apps
from core.dto import FrozenModel
from recipe.dto.ingredient import IngredientDto


class RecipeDto(FrozenModel):
    id: int
    name: str
    description: str
    ingredients: List[IngredientDto]

    @field_validator(__field="ingredients", mode="before")
    @classmethod
    def get_all_ingredients(cls, v: object) -> object:
        if isinstance(v, BaseManager):
            return list(v.all())
        return v

    def to_json(self):
        return self.model_dump()
