import serial
import time
import numpy as np
from collections import deque
import warnings
import itertools
import csv


hw_sensor = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
hw_sensor.setDTR(False)
time.sleep(.1)
hw_sensor.flushInput()
hw_sensor.setDTR(True)

label = 'up_down'
count_file = 6

M = []
data = []

f = open(f'{label}_6.csv', 'a')
w = csv.writer(f)

with hw_sensor:
    while True:
        try:
            line = hw_sensor.readline()
            if not line:
                # HACK: Descartamos líneas vacías porque fromstring produce
                # resultados erróneos, ver https://github.com/numpy/numpy/issues/1714
                continue
            # M.append(np.fromstring(line.decode('ascii', errors='replace'), sep=','))
            # data.append(yy)
            tmp = line.decode('ascii', errors='replace').rstrip().split(',')
            if (len(tmp) >= 5):
                data.append(tmp)

            if (len(data) == 119):
                r = input('¿Guardar?')
                if (r == 's'):
                    w.writerow(list(itertools.chain(*data)) + [label])
                data = []
        except KeyboardInterrupt:
            print("Exiting")
            break
