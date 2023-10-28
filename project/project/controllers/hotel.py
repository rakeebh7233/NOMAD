from tg import expose, request, RestController, validate, redirect
from tg.decorators import with_trailing_slash
# from sqlalchemy import create_engine, Column, Integer, String, DateTime
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from project.model import DBSession, Hotel
from datetime import datetime
import requests

# Base = declarative_base()

# class Hotel(Base):
#     __tablename__ = 'hotels'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     location = Column(String)
#     price = Column(Integer)
#     rooms_available = Column(Integer)
#     check_in_date = Column(DateTime)
#     check_out_date = Column(DateTime)

# engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')
# Session = sessionmaker(bind=engine)

class HotelController(RestController):

    @with_trailing_slash
    @expose('json')
    def get_all(self):
        hotels = DBSession.query(Hotel).all()
        return {[hotel.__dict__ for hotel in hotels]}

    @expose('json')
    def get_one(self, hotel_id):
        hotel = DBSession.query(Hotel).filter_by(id=hotel_id).first()
        if hotel:
            return hotel.to_dict()
        else:
            return {'error': 'Hotel not found'}
    
    @expose('json')
    @validate({
        'name': str,
        'location': str,
        'checkinDate': datetime,
        'checkoutDate': datetime,
        'adults': int,
        'room_qty': int
    })
    def get_hotel(self, name, location, checkinDate, checkoutDate, adults, room_qty):
        hotels = DBSession.query(Hotel).filter_by(name=name, location=location, checkinDate=checkinDate, checkoutDate=checkoutDate, adults=adults, rooms_qty=room_qty).all()
        return {[hotel.__dict__ for hotel in hotels]}

    @expose('json')
    @validate({
        'name': str,
        'location': str,
        'price': int,
        'rooms_qty': int,
        'checkinDate': datetime,
        'checkoutDate': datetime
    })
    def post(self, name, location, price, adults, room_qty, checkinDate, checkoutDate):
        hotel = Hotel(name=name, location=location, price=price, adults=adults, rooms_qty=room_qty, check_in_date=checkinDate, check_out_date=checkoutDate)
        DBSession.add(hotel)
        DBSession.commit()
        return {'message': 'Hotel created successfully'}

    @expose('json')
    @validate({
        'name': str,
        'location': str,
        'price': int,
        'adults': int,
        'rooms_qty': int,
        'checkinDate': datetime,
        'checkoutDate': datetime
    })
    def put(self, name=None, location=None, price=None, adults=None, rooms_qty=None, checkinDate=None, checkoutDate=None):
        hotel = DBSession.query(Hotel).filter_by(name=name).first()
        if not hotel:
            return {'error': 'Hotel not found'}
        if location:
            hotel.location = location
        if price:
            hotel.price = price
        if rooms_qty:
            hotel.rooms_qty = rooms_qty
        if checkinDate:
            hotel.checkinDate = checkinDate
        if checkoutDate:
            hotel.checkoutDate = checkoutDate
        DBSession.commit()
        return {'message': 'Hotel updated successfully'}

    @expose('json')
    def delete(self, name):
        hotel = DBSession.query(Hotel).filter_by(name=name).first()
        if hotel:
            DBSession.delete(hotel)
            DBSession.commit()
            return {'message': 'Hotel deleted'}
        else:
            return {'error': 'Hotel not found'}   


    @expose('json')
    def search_hotels(self, dest, arrival_date, departure_date, adults, room_qty, price_max):

        dest_url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"
        dest_querystring = {"query": dest}

        dest_headers = {
            "X-RapidAPI-Key": "1a662e0bdemsh110faa611833139p1cdab6jsn13e9ab23c24f",
            "X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
        }

        dest_response = requests.get(dest_url, headers=dest_headers, params=dest_querystring)
        dest_id = dest_response.json()['data'][0]['dest_id']
        location = dest_response.json()['data'][0]['name']

        url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels"
        querystring = {
            "arrival_date": arrival_date,
            "departure_date": departure_date,
            "adults": adults,
            "room_qty": room_qty,
            "dest_id": dest_id,
            "price_max": price_max
        }
        headers = {
            "X-RapidAPI-Key": "1a662e0bdemsh110faa611833139p1cdab6jsn13e9ab23c24f",
            "X-RapidAPI-Host": "booking-com.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        hotels_data = response.json()
        for hotel_data in hotels_data['data']['hotels']:
            name = hotel_data['property']['name']
            checkinDate = hotel_data['property']['checkinDate']
            checkoutDate = hotel_data['property']['checkoutDate']
            reviewScore = hotel_data['property']['reviewScore']
            currency = hotel_data['property']['priceBreakdown']['grossPrice']['currency']
            price = hotel_data['property']['priceBreakdown']['grossPrice']['value']
            hotel = Hotel(name=name, location=location, checkinDate=checkinDate, checkoutDate=checkoutDate, adults=adults, room_qty=room_qty, reviewScore=reviewScore, currency=currency, price=price)
            DBSession.add(hotel)
        DBSession.commit()
        return hotels_data


    
