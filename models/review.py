#!/usr/bin/python3
"""define class new"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class that inherit BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
