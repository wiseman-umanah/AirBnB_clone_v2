#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """Table for Amenities"""
    if getenv("HBHNB_TYPE_STORAGE") == "db":
        from models.place import place_amenity
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
