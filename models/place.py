#!/usr/bin/python3
"""place class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """class representation of Place
    Attributes:
        city_id: the city id
        user_id: the user id
        name: username input
        description: description string
        number_rooms: integer value
        number_bathrooms: integer value
        max_guest: integer value
        price_by_night:: price per night
        latitude: float value
        longitude: float value
        amenity_ids: ids list
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ gets a list of review ids """
            _data = models.storage.all()
            _list = []
            _res = []
            for k in var:
                _review = k.replace('.', ' ')
                _review = shlex.split(_review)
                if (_review[0] == 'Review'):
                    _list.append(_data[k])
            for el in _list:
                if (el.place_id == self.id):
                    _res.append(el)
            return (_res)

        @property
        def amenities(self):
            """ gets a list of amenity ids"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ add obj id to amenity """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
