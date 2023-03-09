#!/usr/bin/python3
"""Inherances from Base Model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.place_id = ''
        self.user_id = ''
        self.text = ''
