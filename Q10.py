# WaveStep.py

import time
import board
import digitalio

HIGH = True
LOW = False
DELAY = 0.3

# If L298 driver board enable jumpers are not used, uncomment the lines below with correct pins
#PIN_ENABLE_A = board.D4
#PIN_ENABLE_B = board.TX
PIN_COIL_A1 = board.D13  # IN_1
PIN_COIL_A2 = board.D12  # IN_2
PIN_COIL_B1 = board.D11  # IN_3
PIN_COIL_B2 = board.D10  # IN_4

#enableA = digitalio.DigitalInOut(PIN_ENABLE_A)
#enableB = digitalio.DigitalInOut(PIN_ENABLE_B)
coil_A1 = digitalio.DigitalInOut(PIN_COIL_A1)
coil_A2 = digitalio.DigitalInOut(PIN_COIL_A2)
coil_B1 = digitalio.DigitalInOut(PIN_COIL_B1)
coil_B2 = digitalio.DigitalInOut(PIN_COIL_B2)

#enableA.direction = digitalio.Direction.OUTPUT
#enableB.direction = digitalio.Direction.OUTPUT
coil_A1.direction = digitalio.Direction.OUTPUT
coil_A2.direction = digitalio.Direction.OUTPUT
coil_B1.direction = digitalio.Direction.OUTPUT
coil_B2.direction = digitalio.Direction.OUTPUT

#enableA.value = enableB.value = True

def A1_A2():
    coil_A1.value = HIGH
    coil_A2.value = HIGH
    coil_B1.value = LOW
    coil_B2.value = LOW
    time.sleep(DELAY)
    coil_A1.value = LOW
    coil_A2.value = LOW

def A1():
    coil_A1.value = HIGH
    coil_A2.value = LOW
    coil_B1.value = LOW
    coil_B2.value = LOW
    time.sleep(DELAY)
    coil_A1.value = LOW

def A1_B1():
    coil_A1.value = HIGH
    coil_A2.value = LOW
    coil_B1.value = HIGH
    coil_B2.value = LOW
    time.sleep(DELAY)
    coil_A1.value = LOW
    coil_B1.value = LOW

def B1():
    coil_A1.value = LOW
    coil_A2.value = LOW
    coil_B1.value = HIGH
    coil_B2.value = LOW
    time.sleep(DELAY)
    coil_B1.value = LOW

def B1_A2():
    coil_A1.value = LOW
    coil_A2.value = HIGH
    coil_B1.value = HIGH
    coil_B2.value = LOW
    time.sleep(DELAY)
    coil_A2.value = LOW
    coil_B1.value = LOW

def A2():
    coil_A1.value = LOW
    coil_A2.value = HIGH
    coil_B1.value = LOW
    coil_B2.value = LOW
    time.sleep(DELAY)
    coil_A2.value = LOW

def A2_B2():
    coil_A1.value = LOW
    coil_A2.value = HIGH
    coil_B1.value = LOW
    coil_B2.value = HIGH
    time.sleep(DELAY)
    coil_A2.value = LOW
    coil_B2.value = LOW

def B2():
    coil_A2.value = LOW
    coil_A1.value = LOW
    coil_B1.value = LOW
    coil_B2.value = HIGH
    time.sleep(DELAY)
    coil_B2.value = LOW

# Dictionary of coil energization functions
switcher = {
    1: A1_A2,
    2: A1,
    3: A1_B1,
    4: B1,
    5: B1_A2,
    6: A2,
    7: A2_B2,
    8: B2
}



half_step_list_cw = [1,2,3,4,5,6,7,8]
half_step_list_ccw = [8,7,6,5,4,3,2,1]

def half_step(step):
    if step > 0:
        for i in range(0, step, 1):
            if i > 7:
                # using the modulus to get the reminder and reset the index,
                # since the index of order list can't greater than 3
                j = i%8
            else:
                j = i
            seq = switcher.get(half_step_list_cw[j])
            seq()
    elif step < 0:
         for i in range(0, abs(step), 1):
            if i > 7:
                # using the modulus to get the reminder and reset the index,
                # since the index of order list can't greater than 3
                j = i%8
            else:
                j = i
            seq = switcher.get(half_step_list_ccw[j])
            seq()

while True:
    step = int(input("Enter the step number: "))
    half_step(step)
    print("Cycle Ended")
    time.sleep(2)
