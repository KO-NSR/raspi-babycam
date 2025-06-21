import RPi.GPIO as GPIO
import dht11
import time
import datetime

class DHT11Reader:
    def __init__(self, pin=4):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
        self.instance = dht11.DHT11(pin=self.pin)

    def read(self):
        result = self.instance.read()
        if result.is_valid():
            timestamp = datetime.datetime.now()
            return {
                'timestamp': timestamp,
                'temperature': result.temperature,
                'humidity': result.humidity
            }
        else:
            return None

