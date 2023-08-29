# AN examples of producing a simple beep in a Windows pc.
# This is supposed to simulate the sounds of race starting in older 8 bit video games.

import time as t
import winsound

if __name__== "__main__":
    for i in range(3):
        winsound.Beep(600, 200)
        t.sleep(1)

    winsound.Beep(1200, 500)