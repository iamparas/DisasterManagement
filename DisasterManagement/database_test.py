from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from database_setup import DisasterEvent, Disaster, Base
import data_models_test
engine = create_engine('sqlite:///disastermanagement.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

def set_up_tables():
    for row in data_models_test.data:
        con.execute(text("""INSERT INTO Disaster (id, name)
                            VALUES(:id, :name)"""), **row)

    for row in data_models_test.disaster_event_data:
        con.execute(text("INSERT INTO DisasterEvent(id, title, glide, status, description, date_occured, date_ended, disaster_type) VALUES(:id, :title, :glide, :status, :description, :date_occured, :date_ended, :disaster_type)"), **row)

    for row in data_models_test.location_data:
        con.execute(text("""INSERT INTO Location(id, country, state, city, lat, lon)
                            VALUES(:id, :country, :state, :city, :lat, :lon)"""), **row)
with engine.connect() as con:
    #set_up_tables()
    rows = con.execute(text('SELECT * FROM Disaster'))
    vals = session.query(Disaster).from_statement(text("SELECT * FROM Disaster")).all()
    rows = session.query(DisasterEvent).from_statement(text("SELECT * FROM DisasterEvent")).all()
    print dir(rows)
