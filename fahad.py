import serial
import csv
import time

ser = serial.Serial('COM5', 9600)
time.sleep(2)
ser.flushInput()

with open('fahad.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Timestamp', 'Noise (dB)', 'CO2 (ppm)', 'Temperature (C)'])

    while True:
        line = ser.readline().decode('utf-8').strip()
        print(f"Got line: '{line}'")

        if line:
            data = line.split(',')  # [noise, CO2, temp]
            timestamp = time.strftime("%Y-%m-%d %H:%M")
            writer.writerow([timestamp] + data)
            csvfile.flush()
