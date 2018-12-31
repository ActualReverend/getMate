import serial
def getMate():
    ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
    while True:
        line = ser.readline()   # read a '\n' terminated line
        print(line)
    ser.close()

if __name__ == "__main__":
    getMate()
    pass