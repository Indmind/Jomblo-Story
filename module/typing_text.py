import time
import sys

def textType(text, delay=.1):
    print(' ', end='')
    for i in text:
        print(i, end='')
        sys.stdout.flush()
        if not i == '\n':
            time.sleep(delay)
        if i == ',':
            time.sleep(.4)
