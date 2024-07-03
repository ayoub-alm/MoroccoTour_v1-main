#!/usr/bin/python3
"""class Place Module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


place_facility = Table('place_facility', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('facility_id', String(60),
                                 ForeignKey('facilities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """Place Class definition"""
    __tablename__ = "places"

    name = Column("name", String(128), nullable=False)
    description = Column("description", String(1024))
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)
    city_id = Column("city_id", String(60),
                     ForeignKey("cities.id"), nullable=False)
    user_id = Column("user_id", String(60),
                     ForeignKey("users.id"), nullable=False)
    categorie_id = Column("categorie_id", String(60),
                          ForeignKey("categories.id"), nullable=False)
    reviews = relationship("Review",
                           backref="place",
                           cascade="all, delete, delete-orphan")
    facilities = relationship("Facility",
                                 secondary=place_facility,
                                 viewonly=False)
