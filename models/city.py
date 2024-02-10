#!/usr/bin/python3

"""City Module:
Inherits from the Superclass BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that is inheriting from BaseModel
    with Public class attributes
    """
    state_id: str = ""
    name: str = ""