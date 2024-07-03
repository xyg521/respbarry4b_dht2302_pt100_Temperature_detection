import os
import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT22(board.D4)

try:
    f = open('/home/wl8/zwl_test/Adafruit_CircuitPython_DHT/examples/humidity.csv', 'a+')
    if os.stat('/home/wl8/zwl_test/Adafruit_CircuitPython_DHT/examples/humidity.csv').st_size == 0:
            f.write('Date,Time,Temperature C, Temperature F,Humidity\r\n')
except:
    pass

while True:
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32

        humidity = dht_device.humidity
        print("Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(temperature_c, temperature_f, humidity))
        f.write('{0},{1},{2:0.1f}*C,{3:0.1f}*F,{4:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M:%S'), temperature_c, temperature_f, humidity))
    except RuntimeError as err:
        print(err.args[0])

    time.sleep(5.0)
