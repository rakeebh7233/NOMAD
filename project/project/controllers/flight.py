from tg import expose, request, redirect, validate
from tgext.crud import EasyCrudRestController
from tg.controllers import RestController
from tg.decorators import with_trailing_slash
from project.model import DBSession, Flight
import requests

class FlightController(RestController):

    @with_trailing_slash
    @expose('json')
    def get_all(self):
        flights = DBSession.query(Flight).all()
        return {[f.to_dict() for f in flights]}

    @expose('json')
    def get_one(self, id):
        flight = DBSession.query(Flight).get(id)
        if not flight:
            return {'error': 'Flight not found'}
        return flight.to_dict()
    
    @expose('json')
    def get_flight(self, departureAirport, arrivalAirport, departureTime):
        flight = DBSession.query(Flight).filter_by(departureAirport=departureAirport, arrivalAirport=arrivalAirport, departureTime=departureTime).first()
        if not flight:
            return {'error': 'Flight not found'}
        return flight.to_dict()
    
    @expose('json')
    def post(self, **kwargs):
        # Extract the data from the request
        flight_id = kwargs.get('flight_id')
        departure_airport = kwargs.get('departure_airport')
        arrival_airport = kwargs.get('arrival_airport')
        departure_time = kwargs.get('departure_time')
        arrival_time = kwargs.get('arrival_time')
        cabin_class = kwargs.get('cabin_class')
        carrier = kwargs.get('carrier')
        currency = kwargs.get('currency')
        total_price = kwargs.get('total_price')

        # Create a new Flight object and add it to the database
        flight = Flight(flight_id=flight_id, departureAirport=departure_airport, arrivalAirport=arrival_airport, 
                        departureTime=departure_time, arrivalTime=arrival_time, cabinClass=cabin_class, carrier=carrier, 
                        currency=currency, totalPrice=total_price)
        DBSession.add(flight)
        DBSession.commit()

        # Return the newly created Flight object as JSON
        return flight.to_dict()
    
    
    @expose('json')
    def put(self, id, **kwargs):
        flight = DBSession.query(Flight).get(id)
        if not flight:
            return {'error': 'Flight not found'}

        # Update the flight object with the new data
        flight.flight_id = kwargs.get('flight_id', flight.flight_id)
        flight.departureAirport = kwargs.get('departure_airport', flight.departureAirport)
        flight.arrivalAirport = kwargs.get('arrival_airport', flight.arrivalAirport)
        flight.departureTime = kwargs.get('departure_time', flight.departureTime)
        flight.arrivalTime = kwargs.get('arrival_time', flight.arrivalTime)
        flight.cabinClass = kwargs.get('cabin_class', flight.cabinClass)
        flight.carrier = kwargs.get('carrier', flight.carrier)
        flight.currency = kwargs.get('currency', flight.currency)
        flight.totalPrice = kwargs.get('total_price', flight.totalPrice)

        DBSession.commit()

        # Return the updated flight object as JSON
        return flight.to_dict()
    
    
    @expose('json')
    def delete(self, id):
        flight = DBSession.query(Flight).get(id)
        if not flight:
            return {'error': 'Flight not found'}

        DBSession.delete(flight)
        DBSession.commit()

        return {'message': 'Flight deleted successfully'}

    @expose('json')
    def search_flights(fromAC, toAC, depDate, retDate, adults, cabin):
        url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchFlights"
        querystring = {
            "fromId": fromAC,
            "toId": toAC,
            "departDate": depDate,
            "returnDate": retDate,
            "adults": adults,
            "cabinClass": cabin
        }
        headers = {
            "X-RapidAPI-Key": "1a662e0bdemsh110faa611833139p1cdab6jsn13e9ab23c24f",
            "X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        
        # Store the data from the response in the flights database as a cache 
        flights_data = response.json()
        for flight_data in flights_data['data']['flightOffers']:
            for i in range(2):
                flight_id = flight_data['token']
                departureAirport = flight_data['segments'][i]['departureAirport']['code']
                arrivalAirport = flight_data['segments'][i]['arrivalAirport']['code']
                departureTime = flight_data['segments'][i]['legs'][i]['departureTime']
                arrivalTime = flight_data['segments'][i]['legs'][i]['arrivalTime']
                cabinClass = flight_data['segments'][i]['legs']['cabinClass']
                carrier = flight_data['segments'][i]['legs'][i]['carriersData'][i]['code']
                currency = flight_data['priceBreakdown']['total']['currency']
                totalPrice = flight_data['priceBreakdown']['total']['units']
                flight = Flight(flight_id=flight_id, departureAirport=departureAirport, arrivalAirport=arrivalAirport, 
                                departureTime=departureTime, arrivalTime=arrivalTime, cabinClass=cabinClass, carrier=carrier, 
                                currency=currency, totalPrice=totalPrice)
                DBSession.add(flight)
        DBSession.commit()
        
        return flights_data

 

