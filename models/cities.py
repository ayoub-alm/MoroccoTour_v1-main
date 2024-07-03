#!/usr/bin/python3
""" City class Module """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.places import Place


class City(BaseModel, Base):
    """ Class City difinition """
    __tablename__ = "cities"

    name = Column("name", String(128), nullable=False)
    region_id = Column("region_id", String(60),
                      ForeignKey("regions.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
