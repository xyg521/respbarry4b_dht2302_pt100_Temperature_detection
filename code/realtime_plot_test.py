
import time
import board
import digitalio
import adafruit_max31865
import matplotlib.pyplot as plt

# Create sensor object, communicating over the board's default SPI bus
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=3)
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
# sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=2)

# 创建一个用于绘图的空列表
temperatures = []
times = []
start_time = time.time()

# 设置绘图风格
plt.style.use('bmh')

# 创建一个持续更新的图表
plt.ion()

# Main loop to print the temperature every second.
while True:
    # Read temperature.
    temp = sensor.temperature
    current_time = round(time.time() - start_time, 2)
    
    # 添加温度和时间到列表
    temperatures.append(temp)
    times.append(current_time)
    
    # 绘制图像
    plt.clf()  # 清除之前的图像
    plt.plot(times, temperatures)
    plt.title("Temperature over Time")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Temperature (C)")
    plt.draw()  # 更新图像

    # 暂停一下，让图像有更新的时间
    plt.pause(0.05) 
    # Print the value.
    #print("Temperature: {0:0.3f}C".format(temp))
    #print('Resistance: {0:0.3f} Ohms'.format(sensor.resistance))
    # Delay for a second.
    #time.sleep(2.0)
print("Done")
