from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os, sys

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
