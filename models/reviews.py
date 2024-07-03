#!/usr/bin/python3
""" Class Review module """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.places import Place
from models.users import User


class Review(BaseModel, Base):
    """ Review class definition """
    __tablename__ = "reviews"

    comment = Column("comment", String(1024), nullable=False)
    rating = Column("rating", Integer, default=0)
    user_id = Column("user_id", String(60),
                     ForeignKey("users.id"), nullable=False)
    place_id = Column("place_id", String(60),
                      ForeignKey("places.id"), nullable=False)
