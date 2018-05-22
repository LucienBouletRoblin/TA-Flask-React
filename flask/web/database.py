from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os, sys
import datetime

try:
    POSTGRES_DB = os.environ['POSTGRES_DB']
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
except KeyError:
    print("Please set the environment variable POSTGRES_PASSWORD or POSTGRES_USER or POSTGRES_DB")
    sys.exit(1)

connection_string = 'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@ta-db:5432/{POSTGRES_DB}'.format(
    POSTGRES_PASSWORD=POSTGRES_PASSWORD, POSTGRES_USER=POSTGRES_USER, POSTGRES_DB=POSTGRES_DB)

engine = create_engine(connection_string, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


def init_db():
    from models.user import User
    from models.restaurant import Restaurant
    from models.serving_period import ServingPeriod
    from models.attendance_per_period import AttendancePerPeriod
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures for testing purpose:
    user_1 = User(last_name='aze', first_name="aze", email="aze@aze.aze", username="user1", password=User.generate_hash("user1"))
    db_session.add(user_1)
    user_2 = User(last_name='aze2', first_name="aze2", email="aze2@aze.aze", username="user2", password=User.generate_hash("user2"))
    db_session.add(user_2)
    db_session.commit()

    restaurant_1 = Restaurant(name="restaurant1", email='restaurant@email.com', address="test1 address",
                              user_id=user_1.id)
    db_session.add(restaurant_1)
    restaurant_2 = Restaurant(name="restaurant2", email='restaurant2@email.com', address="test2 address",
                              user_id=user_1.id)
    db_session.add(restaurant_2)
    restaurant_3 = Restaurant(name="restaurant3", email='restaurant3@email.com', address="test3 address",
                              user_id=user_2.id)
    db_session.add(restaurant_3)
    db_session.commit()

    serving_period_1 = ServingPeriod(name="period1", restaurant_id=restaurant_1.id, start=datetime.time(12, 00, 00, 0),
                                     end=datetime.time(15, 00, 00, 0))
    db_session.add(serving_period_1)

    serving_period_2 = ServingPeriod(name="period2", restaurant_id=restaurant_1.id, start=datetime.time(19, 00, 00, 0),
                                     end=datetime.time(23, 00, 00, 0))
    db_session.add(serving_period_2)
    db_session.commit()

    attendance_1 = AttendancePerPeriod(customer=50, date=datetime.date(2018, 2, 2), comment="good day",
                                       serving_period_id=serving_period_2.id)
    db_session.add(attendance_1)
    db_session.commit()
