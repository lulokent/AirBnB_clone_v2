#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ City class representation """
    __tablename__ = 'cities'

    name = Column(String(128),
                    nullable=False)
    state_id = Column(String(60),
                        ForeignKey('states.id'),
                        nullable=False)
    places = relationship('Place', backref='cities',
                            cascade='all, delete, delete-orphan')