from sqlalchemy import Column, Integer, String, Date , ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

from app.database import Base
from app import db_session as db
from app.client import Client

# Define a Feature model
class Feature(Base):

    __tablename__ = 'feature'

    #id primary key
    id = Column(Integer, primary_key=True)

    # Title
    title    = Column(String(128),  nullable=False)

           
    # Product Description
    description    = Column(String(1000),  nullable=True)

    # Title
    title    = Column(String(128),  nullable=False)

    # Client Priority
    client_priority    = Column(Integer,  nullable=False)

    # Target Date
    target_date    = Column(Date,  nullable=False)

    # Ticket URL
    ticket_url    = Column(String(255),  nullable=False)

    #Define relationship between client and feature
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship("Client", back_populates="features")

    # New instance instantiation procedure
    def __init__(self, title, description, client_priority, target_date, ticket_url,client_id):

        self.title     = title
        self.description = description
        self.client_priority     = client_priority
        self.target_date     = target_date
        self.ticket_url     = ticket_url
        c = db.query(Client).get(client_id)
        if(c):
            self.client_id = client_id
            self.client = c

    def __repr__(self):
        return '<Product %r>' % (self.title)  

    def setClient(self, client_id):
        #Saerch the client by id
        c = db.query(Client).get(client_id)
        if(c):
            self.client_id = client_id
            self.client = c
            

