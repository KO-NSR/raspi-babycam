import RPi.GPIO as GPIO
import dht11
import time
import datetime

# GPIOの設定
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# DHT11のインスタンス作成（GPIO4を使用）
instance = dht11.DHT11(pin=4)

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print(f"Last valid input: {datetime.datetime.now()}")
            print(f"Temperature: {result.temperature:.1f}°C")
            print(f"Humidity: {result.humidity:.1f}%")
        time.sleep(6)  # 6秒ごとに測定
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
