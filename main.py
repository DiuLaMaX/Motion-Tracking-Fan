import cv2
import RPi.GPIO as GPIO
import time
from face_detection import FaceDetector
from ultrasonic import Ultrasonic
from fan import Fan
from servo import Servo

# Define boardmode
GPIO.setmode(GPIO.BOARD)

# Define pins
TRIG = 7
ECHO = 11
FAN = 12
DELAY = 0.01
DIST_THRESHOLD = 50
PIN_COIL_A1 = 13  # IN_1
PIN_COIL_A2 = 15  # IN_2
PIN_COIL_B1 = 16  # IN_3
PIN_COIL_B2 = 18  # IN_4


if __name__ == "__main__":
    print("Initializing...")
    detector = FaceDetector()
    ultrasonic = Ultrasonic(TRIG, ECHO)
    fan = Fan(FAN)
    servo = Servo(PIN_COIL_A1, PIN_COIL_A2, PIN_COIL_B1, PIN_COIL_B2, DELAY)
    time.sleep(1.0)
    print("Finished Initialization")
    while True:
        frame, x, y = detector.detect_face()
        cv2.imshow('Frame',frame)
        print(x, y)
        servo.trace(x)
        
        distance = ultrasonic.get_distance()
        print(distance)
        if distance <= DIST_THRESHOLD:
            fan.motor_on()
        else:
            fan.motor_off()
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            detector.stop()
            ultrasonic.stop()
            servo.stop()
            break