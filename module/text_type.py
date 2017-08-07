import time
import sys

def textType(text, delay=.1):
    for i in text:
        print(i, end='')
        sys.stdout.flush()
        time.sleep(delay)
        if i == ',':
            time.sleep(.4)
