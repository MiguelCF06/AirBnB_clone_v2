#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref="state", cascade="all, delete")

    else:
        @property
        def cities(self):
            """Gets cities related to state"""
            city_l = []
            all_cts = models.storage.all(City)
            for city in all_cts.values():
                if city.state_id == self.id:
                    city_l.append(city)
            return city_l
