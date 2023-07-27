from sqlalchemy import Column, Integer, String, Table, ForeignKey
from database_configs.connection import Base
from sqlalchemy.orm import relationship
from datetime import date


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    gender = Column(String)
    age = Column(String)
    Parcel_orders = relationship('FoodParcelOrders', backref='client')



class FoodParcels(Base):
    __tablename__ = "foodParcels"
    id = Column(Integer, primary_key=True, index=True)


class FoodParcelOrders(Base):
    __tablename__ = "FoodParcelOrders"
    id = Column(Integer, primary_key=True, index=True) 
    date_given = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id'))
    parcel_id = Column(Integer, ForeignKey('FoodParcels.id'))