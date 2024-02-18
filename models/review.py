#!/usr/bin/python3
"""module containing Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review"""

    place_id = ""
    user_id = ""
    text = ""
