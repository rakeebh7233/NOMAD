from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary, String, Float
from sqlalchemy.orm import relationship, backref

from project.model import DeclarativeBase, metadata, DBSession

class Hotel(DeclarativeBase):
    __tablename__ = 'hotels'

    name = Column(String(255), nullable=False, primary_key=True)
    location = Column(String(255), nullable=False, primary_key=True)
    checkinDate = Column(String(255), nullable=False)
    checkoutDate = Column(String(255), nullable=False)
    adults = Column(Integer, nullable=False, default=1)
    room_qty = Column(Integer, nullable=False, default=1)
    reviewScore = Column(Float, nullable=False, default=0.0)
    currency = Column(String(255), nullable=False, default='USD')
    price = Column(Float, nullable=False, default=0.0)

    def __init__(self, name, location, checkinDate, checkoutDate, adults, room_qty, reviewScore, currency, price):
        self.name = name
        self.location = location
        self.checkinDate = checkinDate
        self.checkoutDate = checkoutDate
        self.adults = adults
        self.room_qty = room_qty
        self.reviewScore = reviewScore
        self.currency = currency
        self.price = price

    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'checkinDate': self.checkinDate,
            'checkoutDate': self.checkoutDate,
            'adults': self.adults,
            'room_qty': self.room_qty,
            'reviewScore': self.reviewScore,
            'currency': self.currency,
            'price': self.price
        }
    
    def __repr__(self):
        return '<Hotel: %s>' % self.name
    
    def __unicode__(self):
        return self.name
    
    @classmethod
    def get_all(cls):
        return DBSession.query(cls).all()
    
    @classmethod
    def get_by_name(cls, name):
        return DBSession.query(cls).filter(cls.name == name).first()
    
    @classmethod
    def get_by_location(cls, location):
        return DBSession.query(cls).filter(cls.location == location).all()
    
    @classmethod
    def get_by_name_and_location(cls, name, location):
        return DBSession.query(cls).filter(cls.name == name, cls.location == location).first()
    
    @classmethod
    def get_by_name_and_location_and_checkinDate(cls, name, location, checkinDate):
        return DBSession.query(cls).filter(cls.name == name, cls.location == location, cls.checkinDate == checkinDate).first()
    
    @classmethod
    def add_hotel(cls, name, location, checkinDate, checkoutDate, adults, room_qty, reviewScore, currency, price):
        hotel = cls(name=name, location=location, checkinDate=checkinDate, checkoutDate=checkoutDate, adults=adults, room_qty=room_qty, reviewScore=reviewScore, currency=currency, price=price)
        DBSession.add(hotel)
        DBSession.commit()
        return hotel
    
    
    @classmethod
    def update_hotel(cls, name=None, location=None, checkinDate=None, checkoutDate=None, adults=None, room_qty=None, reviewScore=None, currency=None, price=None):
        hotel = cls.get_by_name_and_location(name, location)
        if hotel:
            if name:
                hotel.name = name
            if location:
                hotel.location = location
            if checkinDate:
                hotel.checkinDate = checkinDate
            if checkoutDate:
                hotel.checkoutDate = checkoutDate
            if adults:
                hotel.adults = adults
            if room_qty:
                hotel.room_qty = room_qty
            if reviewScore:
                hotel.reviewScore = reviewScore
            if currency:
                hotel.currency = currency
            if price:
                hotel.price = price
            DBSession.commit()
            return hotel
        else:
            return None
                
    __all__ = ['Hotel']
