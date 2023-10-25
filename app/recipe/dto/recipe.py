# Dependencies
from pydantic.v1 import BaseModel


class RecipeDto(BaseModel):
    class Config:
        frozen = True
        orm_mode = True

    id: int
    name: str
    description: str
