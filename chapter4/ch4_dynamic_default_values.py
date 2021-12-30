import time
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


def list_factory():
    return ["a", "b", "c", "d"]


class Model(BaseModel):
    l: List[str] = Field(default_factory=list_factory)
    d: datetime = Field(default_factory=datetime.now)
    l2: List[str] = Field(default_factory=list)


m = Model()
time.sleep(5)
m2 = Model()
print(m)
print(m2)