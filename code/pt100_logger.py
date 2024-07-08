import time
import board
import digitalio
import adafruit_max31865
import os

spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=3)

try:
    f = open('/home/wl8/pt100/Adafruit_CircuitPython_MAX31865/examples/pt100.csv', 'a+')
    if os.stat('/home/wl8/pt100/Adafruit_CircuitPython_MAX31865/examples/pt100.csv').st_size == 0:
            f.write('Date,Time,Temperature C\r\n')
except:
    pass
# Main loop to print the temperature every second.
while True:
    # Read temperature.
    temp = sensor.temperature
    print("Temperature: {0:0.3f}C".format(temp))
    f.write('{0},{1},{2:0.3f}C\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M:%S'), temp))
    time.sleep(2.0)
