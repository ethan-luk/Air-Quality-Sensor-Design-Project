import influxdb_client
import os
# import time
# import schedule
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv

load_dotenv()

INFLUXDB_TOKEN = os.getenv('INFLUXDB_TOKEN')
ORG = os.getenv('ORG')
URL = os.getenv('URL')

client = influxdb_client.InfluxDBClient(url=URL, token=INFLUXDB_TOKEN, org=ORG)
bucket="sensor_data"
query_api = client.query_api()

query = """pollutant = from(bucket: "sensor_data")
            |> range(start: -2d)
            |> filter(fn: (r) => r["_measurement"] == "Final_Sensor_Data") and r["Pollutant"] == "__category__Pollutant")
            |> filter(fn: (r) => r["_field"] == "Alcohol")
            |> limit(n: 5)

          location = from(bucket: "sensor_data")
            |> range(start: -2d)
            |> filter(fn: (r) => r["_measurement"] == "Final_Sensor_Data" and r["Geolocation] == "Geohash")
            |> filter(fn: (r) => r["_field"] == "Geohash")
            |> limit(n: 5)
          
          join(
              tables: {pol:pollutant, loc=location},
              on: ["_time", "_start"]
          )


  """
tables = query_api.query(query, org=ORG)

for table in tables:
  for record in table.records:
    print(record)

"""Aggregate function (mean) query"""
# query_api = client.query_api()

# query = """from(bucket: "sensor_data")
#   |> range(start: -10m)
#   |> filter(fn: (r) => r._measurement == "measurement1")
#   |> mean()"""
# tables = query_api.query(query, org="atrieu9@gmail.com")

# for table in tables:
#     for record in table.records:
#         print(record)

# Mean of pollutant value based on location
'''
from(bucket: "sensor_data")
 |> range(start: -2d)
 |> filter(fn: (r) => r["_measurement"] == "Final_Sensor_Data")
 |> filter(fn: (r) => r["Pollutant"] == "__category__Pollutant" or r["Geolocation"] == "Geohash")
 |> filter(fn: (r) => r["_field"] == "Alcohol" and r["_field"] == "Geohash")
 |> group(columns: ["Geohash"])
 |> mean(column: "Alcohol")

'''



'''
import "join"
pol = from(bucket: "sensor_data")
            |> range(start: -2d)
            |> filter(fn: (r) => r["_measurement"] == "Final_Sensor_Data" and r["Pollutant"] == "__category__Pollutant")
            |> filter(fn: (r) => r["_field"] == "Smoke")
            |> limit(n: 5)
            |> yield(name: "hi")

loc = from(bucket: "sensor_data")
            |> range(start: -2d)
            |> filter(fn: (r) => r["_measurement"] == "Final_Sensor_Data" and r["Geolocation"] == "Geohash")
            |> filter(fn: (r) => r["_field"] == "Geohash")
            |> limit(n: 5)
            |> yield(name: "bye")
 
join.inner(left:pol, right:loc, on: (l, r) => l["_start"] == r["_start"], as: (l, r) => ({l with label: r["_value"]}))

'''