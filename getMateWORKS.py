import serial
ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
while True:
    line = ser.readline()   # read a '\n' terminated line
    print(line)
ser.close()