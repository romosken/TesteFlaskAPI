from Util import db
from peewee import *


class User(Model):
    id = AutoField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db


class Item(Model):
    id = AutoField()
    owner = ForeignKeyField(User, backref="items")
    title = CharField()
    description = TextField()
    price = DecimalField(auto_round=False, decimal_places=2)

    class Meta:
        database = db


class Trade(Model):
    id = AutoField()
    buyer = ForeignKeyField(User, backref="purchases")
    seller = ForeignKeyField(User, backref="sales")
    item = ForeignKeyField(Item)
    status = CharField()
    price = DecimalField(auto_round=False, decimal_places=2)

    class Meta:
        database = db


# db.connect()
# db.create_tables([User, Item, Trade])
# db.close()
