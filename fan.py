import RPi.GPIO as GPIO
import time

fan = 16 

GPIO.setmode(GPIO.BOARD)

class Fan(object):
    def __init__(self,fan):
        self.fan = fan
        GPIO.setup(self.fan, GPIO.OUT)
        GPIO.output(self.fan, 0)
        
    def motor_on(self):
        GPIO.output(self.fan, 1)
        
    def motor_off(self):
        GPIO.output(self.fan, 0)
        
if __name__ == "__main__":
    print("Start")
    fan = Fan(fan)
    time.sleep(0.1)
    while True:
        fan.motor_on()
        time.sleep(10.0)
        fan.motor_off()
        time.sleep(5.0)
        
    