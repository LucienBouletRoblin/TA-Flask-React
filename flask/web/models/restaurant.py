from sqlalchemy import Column, Integer, Text, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref, validates

from database import Base
from models.user import User


class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text, nullable=True)
    address = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User, backref=backref('restaurants',
                                              uselist=True,
                                              cascade='delete,all'))
