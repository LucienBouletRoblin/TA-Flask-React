from passlib.hash import pbkdf2_sha256
from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from database import Base, db_session


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    last_name = Column(Text)
    first_name = Column(Text)
    email = Column(Text)
    username = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

    restaurant = relationship('Restaurant')

    @hybrid_property
    def display_name(self):
        return self.first_name + ' ' + self.last_name

    def save_to_db(self):
        db_session.add(self)
        db_session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }

        return {'users': list(map(lambda x: to_json(x), User.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db_session.query(cls).delete()
            db_session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}

    @staticmethod
    def generate_hash(password):
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return pbkdf2_sha256.verify(password, hash)


class RevokedTokenModel(Base):
    __tablename__ = 'revoked_tokens'
    id = Column(Integer, primary_key=True)
    jti = Column(String(120))

    def add(self):
        db_session.add(self)
        db_session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
