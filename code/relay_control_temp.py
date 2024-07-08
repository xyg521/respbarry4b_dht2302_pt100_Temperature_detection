import time
import board
import digitalio
import adafruit_max31865
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time
import os

#file = os.open("temperature_data.txt", os.O_CREAT | os.O_TRUNC | os.O_WRONLY)

# Set the GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)
# Define the GPIO pin connected to the relay module's IN pin
RELAY_PIN = 12
# Set the relay pin as an output pin
GPIO.setup(RELAY_PIN, GPIO.OUT)

spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=3)

temperatures = []
times = []
expected_temperatures=[]
start_time = time.time()
plt.style.use('bmh')
# 创建一个持续更新的图表
plt.ion()

# 设置预期温度
EXPECTED_TEMP = 24.0
try:
    while True:
        # 读取温度
        temp = sensor.temperature
        #print("Temperature: {0:0.3f}C".format(temp))
        current_time = round(time.time() - start_time, 2)
        # 添加温度和时间到列表
        temperatures.append(temp)
        times.append(current_time)
        # 添加预期温度到它的列表中
        expected_temperatures.append(EXPECTED_TEMP)
        
        # 绘制图像
        plt.clf()  # 清除之前的图像
        plt.plot(times, temperatures, label='Actual')
        plt.plot(times, expected_temperatures, label='Setpoint')
        plt.title("Temperature over Time")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Temperature (C)")
        plt.draw()  # 更新图像
        # 暂停一下，让图像有更新的时间
        plt.pause(0.1) 

        # 如果读取的温度高于预期温度，关闭继电器（GPIO.HIGH）
        if temp > EXPECTED_TEMP:
            GPIO.output(RELAY_PIN, GPIO.HIGH)
            print("Temperature is higher than expected. Relay is now on.")
        # 如果读取的温度低于或等于预期温度，打开继电器 (GPIO.LOW)
        else:  
            GPIO.output(RELAY_PIN, GPIO.LOW)   
            print("Temperature is equal or lower than expected. Relay is now off.")
        # 每次读取后暂停一秒钟
        time.sleep(1)

except KeyboardInterrupt:
    # 如果用户按下Ctrl+C，就清理GPIO的配置
    GPIO.cleanup()
    # 当程序被用户关闭时，保存图像并退出
    plt.savefig('6.1_1A_tmpmax.png')
    print("Program stopped by user. Final image saved.")
    raise






