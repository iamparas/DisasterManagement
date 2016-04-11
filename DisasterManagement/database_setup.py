from sqlalchemy import Table, Column, ForeignKey, Integer, String, Enum, Float
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()



class Disaster(Base):

    '''Disaster Type Table'''

    __tablename__ = 'Disaster'

    id = Column(Integer, primary_key = True, autoincrement = False)
    name = Column(String, nullable = False)

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name
        }

#association table for many to many relationship between DisasterEvent and Location
association_table = Table('association', Base.metadata,
    Column('event_id', Integer, ForeignKey('DisasterEvent.id')),
    Column('location_id', Integer, ForeignKey('Location.id')))

class DisasterEvent(Base):

    '''Disaster Event Table'''

    __tablename__ = 'DisasterEvent'

    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(80), nullable = False)
    glide = Column(String, nullable = False)                     #global disaster ID number
    status = Column(Enum('current', 'alert', 'past'))
    description = Column(String)
    date_occured = Column(String(11), nullable = False)
    date_ended = Column(String(11))
    disaster_type = Column(String(120), nullable  = False)

    location = relationship("Location", secondary = association_table,
                            back_populates = 'disaster_event')


    @property
    def serialize(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'status' : self.status,
            'description' : self.description
        }

class Location(Base):

    '''Disaster Location Table'''

    __tablename__ = 'Location'

    id = Column(Integer, primary_key = True)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    lat = Column(Float)
    lon = Column(Float)

    disaster_event = relationship("DisasterEvent", secondary = association_table,
                                    back_populates = 'location')
    people = relationship("People", uselist = False,
                            back_populates = 'location')

class People(Base):

    __tablename__ = 'People'

    id = Column(Integer, primary_key = True, autoincrement = True)
    location_id = Column(Integer, ForeignKey('Location.id'))
    num_deaths = Column(Integer)
    num_missing = Column(Integer)
    num_injured = Column(Integer)
    num_affected = Column(Integer)

    location = relationship('Location', back_populates = 'people')

class Home(Base):
    __tablename__ = 'Home'

    id = Column(Integer, primary_key = True)
    num_inhabitable = Column(Integer)
    num_damaged = Column(Integer)
    loss_value = Column(Float)
    loss_value_us = Column(Float)

class Infrastructure(Base):

    __tablename__ = "Infrastructure"

    id = Column(Integer, primary_key = True)
    educational_centres_damaged = Column(Integer)
    hospitals_damaged = Column(Integer)
    roads_damaged = Column(Integer)
    bridges_damaged = Column(Integer)
    water_supply = Column(Integer)
    power_supply = Column(Integer)
    health_sector = Column(Integer)
    loss_value = Column(Float)
    loss_value = Column(Float)


engine = create_engine('sqlite:///disastermanagement.db') #connectts to database
Base.metadata.create_all(engine)
