#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """City getter, relationship between city and
        state for FileStorage"""
        instances = []
        cities = self.all(City)
        for city in cities:
            if city.id == State.id:
                instances.append(city)
        return (instances)
