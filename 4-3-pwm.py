import RPi.GPIO as IO
import time as tm

pin = 24



IO.setmode(IO.BCM)
IO.setup(pin, IO.OUT)

pwm = IO.PWM(pin, 1000)

try:
    while 1:
        print("enter occupancy in range [0:1]")
        occupancy = float(input())
        occupancy = 100 * occupancy
        if occupancy >=0 and occupancy <= 100:
            pwm.start(occupancy)
finally:
    IO.output(pin, 0)
    IO.cleanup()
  