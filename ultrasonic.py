import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
TRIG = 7
ECHO = 11

class Ultrasonic(object):
    def __init__(self, TRIG, ECHO):
        self.TRIG = TRIG
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.output(self.TRIG, 0)
        self.ECHO = ECHO
        GPIO.setup(self.ECHO, GPIO.IN)
        
    def get_distance(self):
        GPIO.output(self.TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, 0)
        while GPIO.input(self.ECHO) == 0:
            pass
        start = time.time()
        while GPIO.input(self.ECHO) == 1:
            pass
        end = time.time()
        distance = (end - start) * 17000
        return distance
    
    def stop(self):
        GPIO.cleanup()
        

if __name__ == "__main__":
    ultrasonic = Ultrasonic(TRIG, ECHO)
    time.sleep(0.1)
    for i in range(10):
        distance = ultrasonic.get_distance()
        print(distance)
        time.sleep(1)
    ultrasonic.stop()
    


      