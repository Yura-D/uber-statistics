from peewee import *


db = PostgresqlDatabase(
    'test',
    user='test',
    password='test',
    host='localhost',
    port=5432
      
)

class TripParameters(Model):
    
    id_session = PrimaryKeyField(null=False)
    addr_start = CharField()
    addr_end = CharField()
    start = CharField()
    end = CharField()
    currency_code = CharField(max_length=5)

    class Meta:
        database = db


class UberPrices(Model):
    
    trip_param = ForeignKeyField(TripParameters, related_name="trip_details")
    time = TimeField()
    distance = FloatField()
    high_estimate = FloatField()
    low_estimate = FloatField()
    duration = IntegerField()
    
    class Meta:
        database = db


if __name__ == "__main__":
    
    db.connect()
    db.create_tables([TripParameters, UberPrices])

