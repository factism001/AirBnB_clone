#!/usr/bin/python3
"""Inherances from Base Model"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        state_id = ''
        name = ''
