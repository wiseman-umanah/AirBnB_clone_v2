#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.review import Review
from models.engine.file_storage import FileStorage


metadata = MetaData()
place_amenity = Table(
    "place_amenity", metadata,
    Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
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
    amenity_ids = []
    review = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    
    @property
    def reviews(self):
        """Reviews getter, relationship between reviews and
        current place for FileStorage"""
        instances = []
        review = FileStorage.all(Review)
        for ref in review:
            if ref.id == Place.id:
                instances.append(ref)
        return (instances)

    @property
    def amenities(self):
        """amenities getter, return the amenity_ids"""
        return self.amenity_ids
    
    @amenities.getter
    def amenities(self):
        """Add a new Amenity instance in amenity_ids"""
        classname = self.__class__.__name__
        if classname == "Amenity":
            self.amenity_ids.append(self.id)
