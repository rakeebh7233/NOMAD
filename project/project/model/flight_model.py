from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary, String, Float
from sqlalchemy.orm import relationship, backref

from project.model import DeclarativeBase, metadata, DBSession

class Flight(DeclarativeBase):
    __tablename__ = 'flight'

    id = Column(Integer, primary_key=True)
    flight_id = Column(String, nullable=False)
    departureAirport = Column(String, nullable=False)
    arrivalAirport = Column(String, nullable=False)
    departureTime = Column(DateTime, nullable=False)
    arrivalTime = Column(DateTime, nullable=False)
    cabinClass = Column(String, nullable=False)
    carrier = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    total_price = Column(Float, nullable=False, default=0.0)

    def __init__ (self, flight_id, departure_airport, arrival_airport, departure_time, arrival_time, cabin_class, carrier, currency, total_price):
        self.flight_id = flight_id
        self.departureAirport = departure_airport
        self.arrivalAirport = arrival_airport
        self.departureTime = departure_time
        self.arrivalTime = arrival_time
        self.cabinClass = cabin_class
        self.carrier = carrier
        self.currency = currency
        self.total_price = total_price

    def to_dict(self):
        return {
            'id': self.id,
            'flight_id': self.flight_id,
            'departure_airport': self.departureAirport,
            'arrival_airport': self.arrivalAirport,
            'departure_time': self.departureTime,
            'arrival_time': self.arrivalTime,
            'cabin_class': self.cabinClass,
            'carrier': self.carrier,
            'currency': self.currency,
            'total_price': self.total_price
        }
    
    def __repr__(self):
        return '<Flight: %s>' % self.flight_id
    
    def __unicode__(self):
        return self.flight_id
    
    @classmethod
    def get_all(cls):
        return DBSession.query(cls).all()
    
    @classmethod
    def get_by_id(cls, id):
        return DBSession.query(cls).get(id)
    
    @classmethod
    def get_by_flight_id(cls, flight_id):
        return DBSession.query(cls).filter(cls.flight_id == flight_id).first()
    
    @classmethod    
    def get_by_airports(cls, departure_airport, arrival_airport):
        return DBSession.query(cls).filter(cls.departureAirport == departure_airport, cls.arrivalAirport == arrival_airport).all()
    
    @classmethod
    def get_by_airports_and_time(cls, departure_airport, arrival_airport, departure_time):
        return DBSession.query(cls).filter(cls.departureAirport == departure_airport, cls.arrivalAirport == arrival_airport, cls.departureTime == departure_time).first()
    
    @classmethod
    def get_by_airports_and_time_range(cls, departure_airport, arrival_airport, departure_time, arrival_time):
        return DBSession.query(cls).filter(cls.departureAirport == departure_airport, cls.arrivalAirport == arrival_airport, cls.departureTime >= departure_time, cls.arrivalTime <= arrival_time).all()
    
    @classmethod
    def get_by_airports_and_time_range_and_cabin_class(cls, departure_airport, arrival_airport, departure_time, arrival_time, cabin_class):
        return DBSession.query(cls).filter(cls.departureAirport == departure_airport, cls.arrivalAirport == arrival_airport, cls.departureTime >= departure_time, cls.arrivalTime <= arrival_time, cls.cabinClass == cabin_class).all()
    
    @classmethod
    def create(cls, flight_id, departure_airport, arrival_airport, departure_time, arrival_time, cabin_class, carrier, currency, total_price):
        new_flight = cls(flight_id=flight_id, departureAirport=departure_airport, arrivalAirport=arrival_airport, departureTime=departure_time, arrivalTime=arrival_time, cabinClass=cabin_class, carrier=carrier, currency=currency, total_price=total_price)
        DBSession.add(new_flight)
        DBSession.commit()
        return new_flight
    
    @classmethod
    def update(cls, id=None, flight_id=None, departure_airport=None, arrival_airport=None, departure_time=None, arrival_time=None, cabin_class=None, carrier=None, currency=None, total_price=None):
        flight = cls.get_by_id(id) if id else cls.get_by_flight_id(flight_id)
        if not flight:
            return None

        if departure_airport:
            flight.departureAirport = departure_airport
        if arrival_airport:
            flight.arrivalAirport = arrival_airport
        if departure_time:
            flight.departureTime = departure_time
        if arrival_time:
            flight.arrivalTime = arrival_time
        if cabin_class:
            flight.cabinClass = cabin_class
        if carrier:
            flight.carrier = carrier
        if currency:
            flight.currency = currency
        if total_price:
            flight.total_price = total_price

        DBSession.commit()
        return flight
    
    
    
    __all__ = ['Flight']
