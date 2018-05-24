from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import ForeignKey

from database import Base


class AttendancePerPeriod(Base):
    __tablename__ = 'attendancePerPeriod'
    id = Column(Integer, primary_key=True)
    customer = Column(Integer)
    date = Column(Date)
    comment = Column(String, nullable=True)
    serving_period_id = Column(Integer, ForeignKey('servingPeriod.id'))
