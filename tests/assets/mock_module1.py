from pydantic import BaseModel, RootModel
from enum import Enum


class E2(Enum):
    pass


class E3(Enum):
    pass


class E4(Enum):
    pass


class X(BaseModel):
    pass


class Y(BaseModel):
    pass


R2 = RootModel[list[int]]