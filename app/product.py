from sqlalchemy import Column, Integer, String
from app.database import Base

# Define a Product model
class Product(Base):

    __tablename__ = 'product'

    #id primary key
    id = Column(Integer, primary_key=True)

    # Product Name
    product_name    = Column(String(128),  nullable=False)

           
    # Product Description
    description    = Column(String(1000),  nullable=True)

    # New instance instantiation procedure
    def __init__(self, product_name, description):

        self.product_name     = product_name
        
        self.description = description

    def __repr__(self):
        return '<Product %r>' % (self.product_name)  
