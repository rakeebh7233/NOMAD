from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary, String, Float
from sqlalchemy.orm import relationship, backref

from project.model import DeclarativeBase, metadata, DBSession

class UserInfo(DeclarativeBase):
    __tablename__ = 'user_info'

    email = Column(String(50), ForeignKey('user_login.email'), primary_key=True)
    first_name = Column(String(50), ForeignKey('user_login.firstName'), nullable=False)
    last_name = Column(String(50), ForeignKey('user_login.lastName'), nullable=False)
    address = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    birthday = Column(DateTime, nullable=False)
    citizenship = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)

    def __init__(self, email, first_name, last_name, address, phone_number, birthday, citizenship):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.birthday = birthday
        self.citizenship = citizenship
        self.address = address


    def to_dict(self):
        return {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'phone_number': self.phone_number,
            'birthday': self.birthday,
            'citizenship': self.citizenship,
            'address': self.address
        }
    
    def __repr__(self):
        return '<UserInfo: %s>' % self.email
    
    def __unicode__(self):
        return self.email
    
    @classmethod
    def get_all(cls):
        return DBSession.query(cls).all()
    
    @classmethod
    def get_by_email(cls, email):
        return DBSession.query(cls).filter(cls.email == email).first()
    
    @classmethod
    def get_by_name(cls, first_name, last_name):
        return DBSession.query(cls).filter(cls.first_name == first_name, cls.last_name == last_name).all()
    
    @classmethod
    def create(cls, email, first_name, last_name, address, phone_number, birthday, citizenship):
        new_user_info = cls(email=email, first_name=first_name, last_name=last_name, address=address, phone_number=phone_number, birthday=birthday, citizenship=citizenship)
        DBSession.add(new_user_info)
        DBSession.commit()
        return new_user_info
    
    @classmethod
    def update_user_info(cls, email, **kwargs):
        user_info = cls.get_by_email(email)
        if user_info:
            for key, value in kwargs.items():
                setattr(user_info, key, value)
            DBSession.commit()
            return user_info
        else:
            return None
        
    __all__ = ['UserInfo']
