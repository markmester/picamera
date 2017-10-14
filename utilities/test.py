from utilities import pantilt
from platform import move
from smbus import SMBus
import time


def test():
    # initialize pantilt class and enable servos
    pwm = pantilt.PanTilt(i2c_bus=SMBus(1))

    pwm.servo_enable(state=True, index=1)
    pwm.servo_enable(state=True, index=2)

    # zeroing out servos
    pwm.servo_one(angle=0)
    pwm.servo_two(angle=0)
    time.sleep(1)

    # handler

    # test
    for i in range(1, 45):
        move(2, 2, pwm)
        time.sleep(.01)

    pwm.servo_one(angle=0)
    pwm.servo_two(angle=0)
    time.sleep(1)

    for i in range(1, 45):
        move(-2, -2, pwm)
        time.sleep(.01)