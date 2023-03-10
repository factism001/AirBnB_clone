#!/usr/bin/python3
"""State class inheritance"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class State"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.name = ''
