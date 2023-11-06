from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary, String, Float
from sqlalchemy.orm import relationship, backref
import bcrypt

from project.model import DeclarativeBase, metadata, DBSession

class UserLogin(DeclarativeBase):
    __tablename__ = 'user_login'

    email = Column(String(100), primary_key=True)
    password = Column(String(100), nullable=False)
    firstName = Column(String(100), nullable=False)
    lastName = Column(String(100), nullable=False)

    def __init__(self, email, password, firstName, lastName):
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName

    def to_dict(self):
        return {
            'email': self.email,
            'password': self.password,
            'firstName': self.firstName,
            'lastName': self.lastName
        }
    
    def __repr__(self):
        return '<UserLogin: %s>' % self.email
    
    def __unicode__(self):
        return self.email
    
    @classmethod
    def get_all(cls):
        return DBSession.query(cls).all()
    
    @classmethod
    def get_by_email(cls, email):
        return DBSession.query(cls).filter(cls.email == email).first()
    
    @classmethod
    def get_by_name(cls, firstName, lastName):
        return DBSession.query(cls).filter(cls.firstName == firstName, cls.lastName == lastName).all()
    
    @classmethod
    def create(cls, email, password, firstName, lastName):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_login = cls(email=email, password=hashed_password, firstName=firstName, lastName=lastName)
        DBSession.add(user_login)
        DBSession.commit()
        return user_login
    
    @classmethod
    def check_credentials(cls, email, password):
        user = cls.get_by_email(email)
        if user:
            hashed_password = user.password.encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return True
        return False
    
    __all__ = ['UserLogin']

