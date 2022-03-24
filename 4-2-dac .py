import RPi.GPIO as IO
import time as tm

def decimal2binary(value):
     
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [10, 9, 11, 5, 6, 13, 19, 26]
dac.reverse()

IO.setmode(IO.BCM)

IO.setup(dac, IO.OUT)

try:
    while(1):
        for i in range(0, 256):
            IO.output(dac, decimal2binary(i))
            tm.sleep(0.001)
            
        
        for i in range(255,-1, -1):
            IO.output(dac, decimal2binary(i))
            tm.sleep(0.001)
finally:
    IO.output(dac, 0)
    IO.cleanup()

