import time
import os
import sys
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
from LCD1602I2C.JLCD import JLCD as LCD
from dht11_reader import DHT11Reader

reader = DHT11Reader(pin=4)
lcd = LCD(2,0x27,True)

try:
    while True:
        data = reader.read()
        if data:
            print(f"Time: {data['timestamp']}")
            print(f"Temperature: {data['temperature']:.1f}°C")
            print(f"Humidity: {data['humidity']:.1f}%")
            lcd.message(f"Temp: {data['temperature']:.1f}゜C",1)
            lcd.message(f"Humi: {data['humidity']:.1f}%",2)
        else:
            print("データ取得に失敗しました")
        time.sleep(6)
except KeyboardInterrupt:
    lcd.clear()
    print("終了処理中...")
    import RPi.GPIO as GPIO
    GPIO.cleanup()

