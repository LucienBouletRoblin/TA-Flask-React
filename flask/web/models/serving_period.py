from sqlalchemy import Column, Integer, String, Time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class ServingPeriod(Base):
    __tablename__ = 'servingPeriod'
    id = Column(Integer, primary_key=True)
    start = Column(Time)
    end = Column(Time)
    name = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

    attendance_per_period = relationship('AttendancePerPeriod')
