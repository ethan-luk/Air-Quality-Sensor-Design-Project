import serial
import time
import schedule
import json

def read_arduino_data():
    connection = serial.Serial(port='COM4', baudrate=9600)
    print('Established serial connection to Arduino')
    arduino_data = connection.readline().decode("UTF-32")  # try with UTF-16 and UTF-32

    try:
        #parse JSON object
        data_parsed = json.loads(arduino_data)
    except json.JSONDecodeError as e:
        print("JSON:", e)

    # arduino.close()
    return data_parsed






# def to_text_file():
#   data = read_arduino_data()
#   with open('data_to_process.txt', 'w') as file:
#     for key, value in data.items():
#         file.write(f'{key}:{value}\n')

# schedule.every(5).seconds.do(read_arduino_data)

# print('Program Started')

# while True:
#     schedule.run_pending()
#     time.sleep(1)