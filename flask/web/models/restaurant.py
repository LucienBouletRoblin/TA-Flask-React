from sqlalchemy import Column, Integer, Text, String, Time, Date
from sqlalchemy import ForeignKey
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


class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text)
    address = Column(String(255))
    user_id = Column(Integer, ForeignKey('user.id'))

    serving_period = relationship('ServingPeriod')


class ServingPeriod(Base):
    __tablename__ = 'servingPeriod'
    id = Column(Integer, primary_key=True)
    start = Column(Time)
    end = Column(Time)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

    attendance_per_period = relationship('AttendancePerPeriod')


class AttendancePerPeriod(Base):
    __tablename__ = 'attendancePerPeriod'
    id = Column(Integer, primary_key=True)
    customer = Column(Integer)
    date = Column(Date)
    serving_period_id = Column(Integer, ForeignKey('servingPeriod.id'))
