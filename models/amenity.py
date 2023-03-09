#!/usr/bin/python3
"""Inherances from Base Model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.name = ''
