import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class Servo(object):
    def __init__(self,PIN_COIL_A1, PIN_COIL_A2, PIN_COIL_B1, PIN_COIL_B2, DELAY=0.3):
        self.PIN_COIL_A1 = PIN_COIL_A1
        self.PIN_COIL_A2 = PIN_COIL_A2
        self.PIN_COIL_B1 = PIN_COIL_B1
        self.PIN_COIL_B2 = PIN_COIL_B2
        self.DELAY = DELAY
        
        GPIO.setup(self.PIN_COIL_A1, GPIO.OUT)
        GPIO.output(self.PIN_COIL_A1, 0)
        GPIO.setup(self.PIN_COIL_A2, GPIO.OUT)
        GPIO.output(self.PIN_COIL_A2, 0)
        GPIO.setup(self.PIN_COIL_B1, GPIO.OUT)
        GPIO.output(self.PIN_COIL_B1, 0)
        GPIO.setup(self.PIN_COIL_B2, GPIO.OUT)
        GPIO.output(self.PIN_COIL_B2, 0)
        
        
        self.switcher = {1: self.A1_A2, 2: self.A1, 3: self.A1_B1, 4: self.B1,
                         5: self.B1_A2, 6: self.A2, 7: self.A2_B2, 8: self.B2}
        self.half_step_list_cw = [1,2,3,4,5,6,7,8]
        self.half_step_list_ccw = [8,7,6,5,4,3,2,1]
        
    def A1_A2(self):
        GPIO.output(self.PIN_COIL_A1, 1)
        GPIO.output(self.PIN_COIL_A2, 1)
        GPIO.output(self.PIN_COIL_B1, 0)
        GPIO.output(self.PIN_COIL_B2, 0)
        time.sleep(self.DELAY)
        GPIO.output(self.PIN_COIL_A1, 0)
        GPIO.output(self.PIN_COIL_A2, 0)

    def A1(self):
        GPIO.output(self.PIN_COIL_A1, 1)
        GPIO.output(self.PIN_COIL_A2, 0)
        GPIO.output(self.PIN_COIL_B1, 0)
        GPIO.output(self.PIN_COIL_B2, 0)
        time.sleep(self.DELAY)
        GPIO.output(self.PIN_COIL_A1, 0)

    def A1_B1(self):
        GPIO.output(self.PIN_COIL_A1, 1)
        GPIO.output(self.PIN_COIL_A2, 0)
        GPIO.output(self.PIN_COIL_B1, 1)
        GPIO.output(self.PIN_COIL_B2, 0)
        time.sleep(self.DELAY)
        GPIO.output(self.PIN_COIL_A1, 0)
        GPIO.output(self.PIN_COIL_B1, 0)

    def B1(self):
        GPIO.output(self.PIN_COIL_A1, 0)
        GPIO.output(self.PIN_COIL_A2, 0)
        GPIO.output(self.PIN_COIL_B1, 1)
        GPIO.output(self.PIN_COIL_B2, 0)
        time.sleep(self.DELAY)
        GPIO.output(self.PIN_COIL_B1, 0)

    def B1_A2(self):
        GPIO.output(self.PIN_COIL_A1, 0)
        GPIO.output(self.PIN_COIL_A2, 1)
        GPIO.output(self.PIN_COIL_B1, 1)
        GPIO.output(self.PIN_COIL_B2, 0)
        time.sleep(self.DELAY)
        GPIO.output(self.PIN_COIL_A2, 0)
        GPIO.output(self.PIN_COIL_B1, 0)

    def A2(self):
        GPIO.output(self.PIN_COIL_A1, 0)
        GPIO.output(self.PIN_COIL_A2, 1)
        GPIO.output(self.PIN_COIL_B1, 0)
        GPIO.output(self.PIN_COIL_B2, 0)
        time.sleep(self.DELAY)
        GPIO.output(self.PIN_COIL_A2, 0)

    def A2_B2(self):
        GPIO.output(self.PIN_COIL_A1, 0)
        GPIO.output(self.PIN_COIL_A2, 1)
        GPIO.output(self.PIN_COIL_B1, 0)
        GPIO.output(self.PIN_COIL_B2, 1)
        time.sleep(self.DELAY)
        GPIO.output(self.PIN_COIL_A2, 0)
        GPIO.output(self.PIN_COIL_B2, 0)

    def B2(self):
        GPIO.output(self.PIN_COIL_A1, 0)
        GPIO.output(self.PIN_COIL_A2, 0)
        GPIO.output(self.PIN_COIL_B1, 0)
        GPIO.output(self.PIN_COIL_B2, 1)
        time.sleep(self.DELAY)
        GPIO.output(self.PIN_COIL_B2, 0)
        
    def move(self, step):
        if step > 0:
            for i in range(0, step, 1):
                if i > 7:
                    j = i%8
                else:
                    j = i
                seq = self.switcher.get(self.half_step_list_cw[j])
                seq()
        elif step < 0:
             for i in range(0, abs(step), 1):
                if i > 7:
                    j = i%8
                else:
                    j = i
                seq = self.switcher.get(self.half_step_list_ccw[j])
                print(seq)
                seq()
    
    def stop(self):
        GPIO.cleanup()
        
        
        
if __name__ == "__main__":
    DELAY = 0.3
    PIN_COIL_A1 = 13  # IN_1
    PIN_COIL_A2 = 15  # IN_2
    PIN_COIL_B1 = 18  # IN_3
    PIN_COIL_B2 = 22  # IN_4
    servo = Servo(PIN_COIL_A1, PIN_COIL_A2, PIN_COIL_B1, PIN_COIL_B2, DELAY)
    servo.move(-10)
    time.sleep(0.1)
    servo.stop()
    