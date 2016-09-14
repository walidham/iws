from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import sessionmaker, relationship

# Define a Client model
class Client(Base):

    __tablename__ = 'client'

    #id primary key
    id = Column(Integer, primary_key=True)

    # Company Name
    company_name    = Column(String(128),  nullable=False)

    # Company email
    email    = Column(String(128),  nullable=False,
                                            unique=True)
    
    # Company Description
    description    = Column(String(1000),  nullable=True)
    
    #Define the relationship between client and feature
    features = relationship("Feature",back_populates="client")


    # New instance instantiation procedure
    def __init__(self, company_name, email, description):

        self.company_name     = company_name
        self.email    = email
        self.description = description

    def __repr__(self):
        return '<Client %r>' % (self.company_name)  
