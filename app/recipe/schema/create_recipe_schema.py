# Dependencies
import jsonref
from pydantic import BaseModel
from typing import List



class IngredientSchema(BaseModel):
    name: str


class CreateRecipeRequestSchema(BaseModel):
    name: str
    description: str
    ingredients: List[IngredientSchema]


class CreateRecipeResponseSchema(CreateRecipeRequestSchema):
    id: str


