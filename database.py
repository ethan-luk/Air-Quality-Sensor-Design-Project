import retrieve_data
import gps
import influxdb_client
import os
import time
import schedule
from influxdb_client import InfluxDBClient, Point, WritePrecision, WriteOptions, WriteApi
import influxdb_client.client.write_api
import pygeohash
from dotenv import load_dotenv

load_dotenv()

bucket="sensor_data"
INFLUXDB_TOKEN = os.getenv('INFLUXDB_TOKEN')
ORG = os.getenv('ORG')
URL = os.getenv('URL')

client = influxdb_client.InfluxDBClient(url=URL, token=INFLUXDB_TOKEN, org=ORG)

write_api = client.write_api(write_options=WriteOptions())

def write_to_database():
  data = retrieve_data.read_arduino_data()
  print(data)
  coord = gps.find_current_location()
  print(coord)

  points = [Point("Final_Sensor_Data").tag("Pollutant", "Alcohol").field("Alcohol", data[0]).field("Geohash", coord),
            Point("Final_Sensor_Data").tag("Pollutant", "Benzene").field("Benzene", data[1]).field("Geohash", coord),
            Point("Final_Sensor_Data").tag("Pollutant", "Hexane").field("Hexane", data[2]).field("Geohash", coord),
            Point("Final_Sensor_Data").tag("Pollutant", "CH4").field("CH4", data[3]).field("Geohash", coord),
            Point("Final_Sensor_Data").tag("Pollutant", "Smoke").field("Smoke", data[4]).field("Geohash", coord),
            Point("Final_Sensor_Data").tag("Pollutant", "CO2").field("CO2", data[5]).field("Geohash", coord),
            Point("Final_Sensor_Data").tag("Pollutant", "Toluene").field("Toluene", data[6]).field("Geohash", coord),
            Point("Final_Sensor_Data").tag("Pollutant", "NH4").field("NH4", data[7]).field("Geohash", coord),
            Point("Final_Sensor_Data").tag("Pollutant", "Acetone").field("Acetone", data[8]).field("Geohash", coord),
            Point("Final_Sensor_Data").tag("Pollutant", "CO").field("CO", data[9]).field("Geohash", coord),
            Point("Final_Sensor_Data").tag("Pollutant", "FG").field("FG", data[10]).field("Geohash", coord)]

  # points = [Point("Final_Sensor_Data").tag("Pollutant", "__category__Pollutant").field("Alcohol", data[0]),
  #           Point("Final_Sensor_Data").tag("Pollutant", "__category__Pollutant").field("Benzene", data[1]),
  #           Point("Final_Sensor_Data").tag("Pollutant", "__category__Pollutant").field("Hexane", data[2]),
  #           Point("Final_Sensor_Data").tag("Pollutant", "__category__Pollutant").field("CH4", data[3]),
  #           Point("Final_Sensor_Data").tag("Pollutant", "__category__Pollutant").field("Smoke", data[4]),
  #           Point("Final_Sensor_Data").tag("Pollutant", "__category__Pollutant").field("CO2", data[5]),
  #           Point("Final_Sensor_Data").tag("Pollutant", "__category__Pollutant").field("Toluene", data[6]),
  #           Point("Final_Sensor_Data").tag("Pollutant", "__category__Pollutant").field("NH4", data[7]),
  #           Point("Final_Sensor_Data").tag("Pollutant", "__category__Pollutant").field("Acetone", data[8]),
  #           Point("Final_Sensor_Data").tag("Pollutant", "__category__Pollutant").field("CO", data[9]),
  #           Point("Final_Sensor_Data").tag("Pollutant", "__category__Pollutant").field("FG", data[10]),
  #           Point("Final_Sensor_Data").tag("Geolocation", "Geohash").field("Geohash", coord)]


            # Point("Final_Sensor_Data").tag("Geolocation", "Latitude").field("Latitude", coord["location"]["lat"]),
            # Point("Final_Sensor_Data").tag("Geolocation", "Longitude").field("Longitude", coord["location"]["lng"]),
            # Point("Final_Sensor_Data").tag("Geolocation", "Accuracy").field("Accuracy", coord["accuracy"]
            
            



  # data_dict = [{"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
  #                "fields": {"Alcohol": data[0]}, "time": 1},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
  #             "fields": {"Benzene": data[1]}, "time": 2},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
  #             "fields": {"Hexane": data[2]}, "time": 3},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
  #             "fields": {"CH4": data[3]},"time": 4},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
  #             "fields": {"Smoke": data[4]}, "time": 5},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
  #             "fields": {"CO2": data[5]}, "time": 6},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
  #             "fields": {"Toluene": data[6]}, "time": 7},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
  #             "fields": {"NH4": data[7]}, "time": 8},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
  #             "fields": {"Acetone": data[8]}, "time": 9},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
  #             "fields": {"CO": data[9]}, "time": 10},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Pollutant": "__category__Pollutant"}, 
  #             "fields": {"FG": data[10]}, "time": 11},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Geolocation": "Latitude"}, 
  #             "fields": {"Latitude": coord["location"]["lat"]}, "time": 12},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Geolocation": "Longitude"}, 
  #             "fields": {"Longitude": coord["location"]["lng"]}, "time": 13},
  #             {"measurement": "Final_Sensor_Data", "tags": {"Geolocation": "Accuracy"}, 
  #             "fields": {"Accuracy": coord["accuracy"]}, "time": 14} ]





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
  write_api.write(bucket=bucket, org=ORG, record=points, database='sensor_data')

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


schedule.every(10).seconds.do(write_to_database)

while True:
    schedule.run_pending()
    time.sleep(1)

