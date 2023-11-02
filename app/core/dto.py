# Dependencies
from pydantic import BaseModel


class FrozenModel(BaseModel):
    class Config:
        frozen = True
        from_attributes = True
