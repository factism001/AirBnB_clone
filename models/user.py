#!/usr/bin/python3
"""Module for user inherence"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class User"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
