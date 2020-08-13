import os
import logging
from datetime import datetime
from flask import Flask, jsonify
from flask_restful import Resource, Api
from peewee import OperationalError
from playhouse.shortcuts import model_to_dict
from marshmallow import Schema, fields, ValidationError

from models import DataPoint


class DataPointSchema(Schema):
    temperature = fields.Float()
    humidity = fields.Float()

    @post_load
    def make_datapoint(self, data, **kwargs):
        return DataPoint(**data)


if os.environ['APP_PATH']:
    logging_path = os.environ['APP_PATH']
else:
    logging_path = os.path.expanduser('~')

# Set up logging
logging.basicConfig(filename=os.path.join(logging_path, 'weather_monitor.log'), level=logging.DEBUG)
logging.debug('Starting up at '.format(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M%S.%f')))

app = Flask(__name__)
api = Api(app)


# Receive temperature and humidity data
class WeatherData(Resource):
    def post(self, temperature, humidity):
        json_data = request.get_json()
        
        try:
            data = DataPointSchema(json_data)
            new_dat_point
            new_data_point = DataPoint.create(
                    created = datetime.now(),
                    temperature = data['temperature'],
                    humidity = data['humidity'])
            logging.debug('Created record: ' + datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M%S.%f'))
        except ValidationError as e:
            logging.debug('Validation error ', e.messages, datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M%S.%f'))
            return e.messages, 422
        except IntegrityError as e:
            logging.debug('Failed to add record. {} {}'.format(', '.join(map(str, data_point)), datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M%S.%f')))
            return 500
        return data_point, 201

    def get(self):
        try:
            all_data = DataPoint.select().get()
            return jsonify(all_data)
        except DataPoint.DoesNotExist as e:
            return {'error': 'that does not exist'}

class WeatherDataFiltered(Resource):
    def get(self, start_date, end_date):
        return {'data': 'goes here', 'start_date': start_date, 'end_date': end_date}

api.add_resource(WeatherData, '/', '/<float:temperature>/<float:humidity>')
api.add_resource(WeatherDataFiltered, '/filter/<string:start_date>/<string:end_date>')

if __name__ == '__main__':
    try:
        DataPoint.create_table()
    except OperationalError:
        print('Entry table already exists.')

    app.run(host='0.0.0.0')

