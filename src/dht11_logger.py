import time
import os
import sys
from dht11_reader import DHT11Reader

DATA_DIR = "/var/www/html/data"
TEMP_FILE = os.path.join(DATA_DIR, "temp.txt")
HUMI_FILE = os.path.join(DATA_DIR, "humi.txt")

def save_data(temperature, humidity):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(TEMP_FILE, "w") as tf:
        tf.write(str(temperature))
    with open(HUMI_FILE, "w") as hf:
        hf.write(str(humidity))

def main():
    reader = DHT11Reader(pin=4)
    while True:
        result = reader.read()
        if result:
            print(f"[{result['timestamp']}] Temp: {result['temperature']}°C  Humi: {result['humidity']}%")
            save_data(result['temperature'], result['humidity'])
        else:
            print("センサー読み取り失敗。")
        time.sleep(5)

if __name__ == "__main__":
    main()
