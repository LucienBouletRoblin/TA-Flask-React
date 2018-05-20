from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    first_name = Column(Text)
    password = Column(String)
    email = Column(Text)

    restaurants = relationship('Restaurant')

    @hybrid_property
    def display_name(self):
        return self.first_name + ' ' + self.name
