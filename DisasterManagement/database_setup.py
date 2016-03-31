from sqlalchemy import Column, ForeignKey, Integer, String
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


class DisasterEvent(Base):

    '''Disaster Event Table'''

    __tablename__ = 'DisasterEvent'

    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(80), nullable = False)
    date = Column(String(11), nullable = False)
    disaster_id  = Column(Integer, ForeignKey('Disaster.id'))
    disaster_event = relationship(Disaster)

    @property 
    def serialize(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'date' : self.date
        }

engine = create_engine('sqlite:///disastermanagement.db') #connectts to database
Base.metadata.create_all(engine)