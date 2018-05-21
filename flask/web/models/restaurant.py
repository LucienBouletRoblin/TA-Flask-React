from sqlalchemy import Column, Integer, Text, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text)
    address = Column(String(255))
    user_id = Column(Integer, ForeignKey('user.id'))

    serving_period = relationship('ServingPeriod')
