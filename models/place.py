#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import relationship
from os import getenv
import models


if getenv("HBHNB_TYPE_STORAGE") == "db":
    place_amenity = Table(
        "place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
            primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
            primary_key=True, nullable=False)
    )


class Place(BaseModel, Base):
    """ A place to stay """
    if getenv("HBHNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1924))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        review = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                backref="place_amenities",
                                viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Reviews getter, relationship between reviews and
            current place for FileStorage"""
            from models.review import Review
            instances = []
            review = models.storage.all(Review)
            for ref in review:
                if ref.id == self.id:
                    instances.append(ref)
            return (instances)

        @property
        def amenities(self):
            """amenities getter, return the amenity_ids"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Add a new Amenity instance in amenity_ids"""
            if obj is not None:
                if obj["__class__"] == "Amenity":
                    self.amenity_ids.append(obj.id)
