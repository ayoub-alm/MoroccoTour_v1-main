#!/usr/bin/python3
""" Category class module """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.places import Place
import models


class Category(BaseModel, Base):
    """ Category class definition """
    __tablename__ = "categories"

    name = Column("name", String(128), nullable=False)
    places = relationship("Place", backref="category", cascade="delete")
