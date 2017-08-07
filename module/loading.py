import time
import sys

def createDots(length, delay):
    for i in range(length):
        print('.', end='')
        sys.stdout.flush()
        time.sleep(delay)

def createHash(length, delay):
    for i in range(length):
        print('#', end='')
        sys.stdout.flush()
        time.sleep(delay)

def createVrDots(length, delay):
    for i in range(length):
        print('.')
        time.sleep(delay)

def deGa():
    time.sleep(.3)
