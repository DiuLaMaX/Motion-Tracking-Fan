import cv2
import RPi.GPIO as GPIO
import time
from face_detection import FaceDetector
from ultrasonic import Ultrasonic
from fan import Fan

GPIO.setmode(GPIO.BOARD)
TRIG = 7
ECHO = 11
FAN = 16


if __name__ == "__main__":
    detector = FaceDetector()
    ultrasonic = Ultrasonic(TRIG, ECHO)
    fan = Fan(FAN)
    time.sleep(2.0)
    while True:
        frame, x, y = detector.detect_face()
        cv2.imshow('Frame',frame)
        print(x, y)
        distance = ultrasonic.get_distance()
        print(distance)
        if distance <= 100:
            fan.motor_on()
        else:
            fan.motor_off()
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            detector.stop()
            ultrasonic.stop()
            break