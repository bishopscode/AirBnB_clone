#!/usr/bin/python3
"""
Module Docs
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class Docs
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
