from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from database_setup import DisasterEvent, Disaster, Base

engine = create_engine('sqlite:///disastermanagement.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()


with engine.connect() as con:
    # data = ({"id" : 4123, "name" : "EarthQuake"},
    #         {"id" : 4143, "name" : "Volcanic Eruption"},
    #         {"id" : 4121, "name" : "Mass Shooting"},
    #         {"id" : 4166, "name" : "Hurricane"},
    #         {"id" : 4187, "name" : "Extreme Heat Waves"},
    #         {"id" : 4133, "name" : "Distro"},
    #         {"id" : 4001, "name" : "Bistro"},

    #     )

    # for row in data:
    #     con.execute(text("""INSERT INTO Disaster (id, name) 
    #                         VALUES(:id, :name)"""), **row)

    rows = con.execute(text('SELECT * FROM Disaster'))
    vals = session.query(Disaster).from_statement(text("SELECT * FROM Disaster")).all()
    print vals
    #print session.query(Disaster).all()
