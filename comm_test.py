import sys
import os
import time

__author__ = 'andymhan'
# Output example: [=======   ] 75%
# width defines bar width
# percent defines current percentage

def progress(width, percent):
    linestr = "\r%s %d%%\r"%(('%%-%ds' % width) % (int(width * percent/100) * '='), percent)
    os.write(1,bytes(linestr, 'UTF-8'))
    sys.stdout.flush()
    if percent >= 100:
        print
        sys.stdout.flush()


# Simulate doing something ...
for i in range(100):
    progress(100, (i + 1))
    time.sleep(0.1) # Slow it down for demo