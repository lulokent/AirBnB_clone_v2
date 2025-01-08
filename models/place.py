#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship
from os import getenv
import models


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place.id', String(60),
                                 ForeignKey('place.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """ Defines a Place class"""
    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60),
                         ForeignKey('cities.id'),
                         nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id'),
                         nullable=False)
        name = Column(String(60),
                      nullable=True)
        description = Column(String(1024),
                             nullable=True)
        number_rooms = Column(Integer,
                              nullable=False,
                              default=0)
        number_bathrooms = Column(Integer,
                                  nullable=False,
                                  default=0)
        max_guest = Column(Integer,
                           nullable=False,
                           default=0)
        price_by_night = Column(Integer,
                                nullable=False,
                                default=0)
        latitude = Column(Float,
                          nullable=True)
        longitude = Column(Float,
                           nullable=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
