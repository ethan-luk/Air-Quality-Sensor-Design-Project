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

"""Simple query"""
query_api = client.query_api()

# when querying might want to do aggregation (mean)

query = """from(bucket: "sensor_data")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
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

'''
from(bucket: "sensor_data")
  |> range(start: -24h)
  |> filter(fn: (r) => r._measurement == "Final_Sensor_Data" and r._tag == "Pollutant")
  |> filter(fn: (r) => r._field == "Alcohol")
  |> mean()

'''
