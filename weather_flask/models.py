import os
import datetime

from peewee import Model, DateTimeField, FloatField, OperationalError, SqliteDatabase


if os.environ['FLASK_DB_PATH']:
    db_path = os.environ['FLASK_DB_PATH']
else:
    db_path = os.path.expanduser('~')


db = SqliteDatabase(os.path.join(db_path, 'temp_data.db'))


class DataPoint(Model):
    created = DateTimeField(default=datetime.datetime.now)
    temperature = FloatField()
    humidity = FloatField()

    class Meta:
        database = db

