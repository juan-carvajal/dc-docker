from typing import Union
from pydantic import BaseModel


class Weather(BaseModel):
    gmat: int
    gpa: float
    work_experience: int