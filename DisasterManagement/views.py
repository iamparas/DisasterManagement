import os
import sys
import json
from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, request, g
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from database_setup import DisasterEvent, Disaster, Base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///disastermanagement.db')


app = Flask(__name__)
api = Api(app)

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, help='Email Address to Create user')
            parser.add_argument('date', type=str, help='Password to create user')
            args = parser.parse_args()
            return {'message': 'Success Entry Added'}
        except Exception as e:
            return {'error':str(e)}

    def get(self):
        try:
            with engine.connect() as con:
                values = session.query(Disaster).from_statement(text("SELECT * FROM Disaster")).all()
                return jsonify(DisasterList = [i.serialize for i in values])
        except Exception as e:
            return {'error' : str(e)}
api.add_resource(CreateUser, '/CreateUser')

if __name__ =='__main__':
    app.run(host="127.0.0.1", port=8010, debug=True)