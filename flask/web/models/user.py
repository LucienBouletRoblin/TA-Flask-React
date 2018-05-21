from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    last_name = Column(Text)
    first_name = Column(Text)
    email = Column(Text)

    restaurant = relationship('Restaurant')

    @hybrid_property
    def display_name(self):
        return self.first_name + ' ' + self.last_name
