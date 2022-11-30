import serial
import time


hw_sensor = serial.Serial(port='COM6', baudrate=9600)
hw_sensor.flushInput()
time.sleep(.1)

file_name = 'up_down_5.csv'

f = open(file_name, 'w', newline='')
f.write("aX,aY,aZ,gX,gY,gZ\n")

while True:
    while hw_sensor.inWaiting():
        try:
            line = hw_sensor.readline().decode('ascii', errors='replace')
            print(line, end='')
            f.write(line)
        except serial.SerialException:
            pass
        except KeyboardInterrupt:
            f.close()
            hw_sensor.close()
