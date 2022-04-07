import RPi.GPIO as IO
import time as tm

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
comp = 4
troyka = 17
dac = [10, 9, 11, 5, 6, 13, 19, 26]
dac.reverse()

IO.setmode(IO.BCM)
IO.setup(troyka, IO.OUT, initial = IO.HIGH)
IO.setup(dac, IO.OUT)
IO.setup(comp, IO.IN)

def adc():
    for i in range(256):
        IO.output(dac, decimal2binary(i))
        tm.sleep(0.001)
        comp_out = IO.input(comp)
        tm.sleep(0.001)
        if comp_out == 0:
            IO.output(dac, 0)
            tm.sleep(0.01)
            return i

    IO.output(dac, 0)
    tm.sleep(0.01)
    return 256





try:
    while(1):
        val = adc()
        print(str(val) +" " + str(float(val) /256 * 3.3))
        tm.sleep(0.001)
finally:
    IO.output(dac, 0)
    IO.cleanup()

