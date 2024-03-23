#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv("HBHNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """City getter, relationship between city and
            state for FileStorage"""
            from models.city import City
            instances = []
            cities = models.storage.all(City)
            
            for city in cities:
                if cities[city].state_id == self.id:
                    instances.append(cities[city])
            return (instances)
