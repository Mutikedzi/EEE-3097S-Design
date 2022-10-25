from glob import escape
import serial
import csv
import numpy
from Crypto.Cipher import AES
from base64 import b64encode


serialPort = serial.Serial(port = "COM3", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serialString = ""                           # Used to hold data coming over UART
fieldsH = ['Time (ms)','Gyro X (dps)','Gyro Y (dps)','Gyro Z (dps)']

with open ('gyro.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fieldsH)

while(1):
    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        if  (len(serialString.decode("utf-8"))>5):
            rows = serialString.decode('utf-8').split(",")
            with open ('gyro.csv' , 'a' ,newline='') as f:
                # Read data out of the buffer until a carraige return / new line is found
                writer = csv.writer(f,delimiter=',', escapechar="%")
                writer.writerow(rows)
                # Print the contents of the serial data
            print(serialString.decode('latin-1')) 
            
