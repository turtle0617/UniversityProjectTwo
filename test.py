import sys
import time
import serial



def main():
        ser = serial.Serial('/dev/ttyACM0', 9600)
        score = ser.readline()
        print score
        print score.split()
while True:
    main()
