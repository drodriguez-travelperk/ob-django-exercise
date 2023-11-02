# Apps
from core.dto import FrozenModel


class IngredientDto(FrozenModel):
    id: int
    name: str
