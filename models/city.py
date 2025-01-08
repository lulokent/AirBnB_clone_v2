#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from os import getenv


class City(BaseModel, Base):
    """ City class representation """
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128),
                      nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id'),
                          nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        state_id = ""
        name = ""
