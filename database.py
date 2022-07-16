import retrieve_data
import gps
import influxdb_client
import os
import time
import schedule
from influxdb_client import InfluxDBClient, Point, WritePrecision, WriteOptions
import influxdb_client.client.write_api
from dotenv import load_dotenv

load_dotenv()

INFLUXDB_TOKEN = os.getenv('INFLUXDB_TOKEN')
ORG = os.getenv('ORG')
URL = os.getenv('URL')

client = influxdb_client.InfluxDBClient(url=URL, token=INFLUXDB_TOKEN, org=ORG)
bucket="sensor_data"

with client.write_api(write_options=WriteOptions(batch_size=200, flush_interval= 1000)) as write_api:  # WriteOptions = batching

  def write_to_database():
    data = retrieve_data.read_arduino_data()
    coord = gps.find_current_location()

    '''
    Old Format of data written to Influx - Data Point structure 

    > Use tags to be able to filter your data easier

    record_name = Point("measurement_name").tag("tag_key_to_identify_data", "tag_value").field("field_key_to_identify_data", "value_of_data")
    write_api.write(bucket=bucket, org=ORG, record=record_name)

    ex. alc = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("Alcohol", data["alcohol"])
        write_api(bucket=bucket, org=ORG, record=alc)
    '''


    '''
    New format takes advantage of Batch Write Option 
    '''
    write_api.write(bucket, ORG, [{"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
                                   "fields": {"Alcohol": data["alcohol"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
                                   "fields": {"Benzene": data["benzene"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
                                   "fields": {"Hexane": data["hexane"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
                                   "fields": {"CH4": data["ch4"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
                                   "fields": {"Smoke": data["smoke"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
                                   "fields": {"CO2": data["co2"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
                                   "fields": {"Toluene": data["toluene"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
                                   "fields": {"NH4": data["nh4"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
                                   "fields": {"Acetone": data["acetone"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
                                   "fields": {"CO": data["co"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
                                   "fields": {"FG": data["fg"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Geolocation": "Latitude"}, 
                                   "fields": {"Latitude": coord["location"]["lat"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Geolocation": "Longitude"}, 
                                   "fields": {"Longitude": coord["location"]["lng"]},
                                   "measurement": "Final_Sensor_Data", "tags": {"Geolocation": "Accuracy"}, 
                                   "fields": {"Accuracy": coord["accuracy"]}}] )

    # MQ Sensor Readings
    # alc = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("Alcohol", data["alcohol"])
    # write_api(bucket=bucket, org=ORG, record=alc)

    # benz = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("Benzene", data["benzene"])
    # write_api(bucket=bucket, org=ORG, record=benz)

    # hex = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("Hexane", data["hexane"])
    # write_api(bucket=bucket, org=ORG, record=hex)

    # ch4 = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("CH4 ", data["ch4"])
    # write_api(bucket=bucket, org=ORG, record=ch4)

    # smoke = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("Smoke", data["smoke"])
    # write_api(bucket=bucket, org=ORG, record=smoke)

    # co2 = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("CO2", data["co2"])
    # write_api(bucket=bucket, org=ORG, record=co2)

    # tol = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("Toluene", data["toluene"])
    # write_api(bucket=bucket, org=ORG, record=tol)

    # nh4 = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("NH4", data["nh4"])
    # write_api(bucket=bucket, org=ORG, record=nh4)

    # ace = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("Acetone", data["acetone"])
    # write_api(bucket=bucket, org=ORG, record=ace)

    # co = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("CO", data["co"])
    # write_api(bucket=bucket, org=ORG, record=co)

    # fg = Point("Final_Sensor_Data").tag("Pollutant", "__category__ Pollutant").field("FG", data["fg"])
    # write_api(bucket=bucket, org=ORG, record=fg)


    # # GPS Coordinate Readings
    # lat = Point("Final_Sensor_Data").tag("Geolocation", "Latitude").field("Latitude", coord[0])
    # write_api(bucket=bucket, org=ORG, record=lat)
    # long = Point("Final_Sensor_Data").tag("Geolocation", "Longitude").field("Longitude", coord[1])
    # write_api(bucket=bucket, org=ORG, record=long)

    # photoresistor_val = Point("TEST Photoresistor").tag("hi", "bye").field("value", data["hi"])
    # write_api.write(bucket=bucket, org=ORG, record=photoresistor_val)
    # number_val = Point("TEST Photoresistor").tag("hi", "BALLS").field("not value", data["hi"])
    # write_api.write(bucket=bucket, org=ORG, record=number_val)


  schedule.every(5).seconds.do(write_to_database)

while True:
    schedule.run_pending()
    time.sleep(1)

