from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary, String, Float
from sqlalchemy.orm import relationship, backref

from project.model import DeclarativeBase, metadata, DBSession

class UserFinances(DeclarativeBase):
    __tablename__ = 'user_finances'
    email = Column(String(100), ForeignKey('user_login.email'), primary_key=True)
    yearly_income = Column(Float)
    monthly_spending = Column(Float)
    estimated_savings = Column(Float)
    monthly_savings_goal = Column(Float)
    travel_budget = Column(Float)

    def __init__(self, email, yearly_income, monthly_spending, estimated_savings, monthly_savings_goal, travel_budget):
        self.email = email
        self.yearly_income = yearly_income
        self.monthly_spending = monthly_spending
        self.estimated_savings = estimated_savings
        self.monthly_savings_goal = monthly_savings_goal
        self.travel_budget = travel_budget

    def to_dict(self):
        return {
            'email': self.email, 
            'yearly_income': self.yearly_income,
            'monthly_spending': self.monthly_spending,
            'estimated_savings': self.estimated_savings,
            'monthly_savings_goal': self.monthly_savings_goal,
            'travel_budget': self.travel_budget
        }
    
    def __repr__(self):
        return '<UserFinances: %s>' % self.email
    
    def __unicode__(self):
        return self.email
    
    @classmethod
    def get_all(cls):
        return DBSession.query(cls).all()
    
    @classmethod
    def get_by_email(cls, email):
        return DBSession.query(cls).filter(cls.email == email).first()
    
    @classmethod
    def create(cls, email, yearly_income, monthly_spending, estimated_savings, monthly_savings_goal, travel_budget):
        user_finances = cls(email=email, yearly_income=yearly_income, monthly_spending=monthly_spending, estimated_savings=estimated_savings, monthly_savings_goal=monthly_savings_goal, travel_budget=travel_budget)
        DBSession.add(user_finances)
        DBSession.commit()
        return user_finances
    
    
    @classmethod
    def update_user_finances(cls, email, **kwargs):
        user_finances = cls.get_by_email(email)
        if user_finances:
            for key, value in kwargs.items():
                setattr(user_finances, key, value)
            DBSession.commit()
            return user_finances 
        else:
            return None
        
    __all__ = ['UserFinances']
