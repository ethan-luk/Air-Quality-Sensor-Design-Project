import serial
import time
import schedule
import json

def main_func():
    arduino = serial.Serial('COM4', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()
    json_object = json.loads(arduino_data)
    print(json_object)

    arduino.close()

list_values = []
list_in_floats = []

print('Program Started')

schedule.every(1).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)