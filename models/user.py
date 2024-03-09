#!/usr/bin/python3

"""
Module for the user class
"""
from models.base_model import BaseModel

class User(BaseModel):
    """This Class defines User Class which has public class attributes
    - email: string - empty string
    - password: string - empty string
    - first_name: string - empty string
    - last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
