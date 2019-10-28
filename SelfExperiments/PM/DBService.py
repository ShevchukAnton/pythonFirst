import datetime

from peewee import *

db = SqliteDatabase('creds.db')


class Accounts(Model):
    name = CharField()
    length = IntegerField(default=20)
    symbols = BooleanField(default=True)
    created_date = DateTimeField(default=datetime.datetime.now)
    p_hash = CharField()

    class Meta:
        database = db
