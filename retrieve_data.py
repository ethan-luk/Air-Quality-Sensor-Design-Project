import serial
import time
import schedule
import json

def read_arduino_data():
    connection = serial.Serial(port='COM4', baudrate=9600)
    print('Established serial connection to Arduino')
    arduino_data = connection.readline().decode("UTF-8")
    
    data_split = arduino_data.split(",")
    float_data = []

    for i in range(len(data_split)):
        float_data.append(float(data_split[i]))
    # cleaned = data_split.replace("\r\n","")

    return float_data

# read_arduino_data()


#Arduino output in JSON format
    #print(arduino_data)
    # try:
    #     #parse JSON object
    #     data_parsed = json.loads(arduino_data)
    # except json.JSONDecodeError as e:
    #     print("JSON:", e)

    # #connection.close()
    # return data_parsed


# schedule.every(5).seconds.do(read_arduino_data)

# print('Program Started')

# while True:
#     schedule.run_pending()
#     time.sleep(1)