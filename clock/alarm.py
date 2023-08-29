import time as t
import winsound

# seconds = int(input("How many seconds to wait"))

circuits = 4
each_apec = 20
apec_rest = 10
rest = 30
corrective = 30

def ape_phase():
    winsound.Beep(600, 1000)
    print("APE")
    for i in range(each_apec):
        t.sleep(1)
    winsound.Beep(440, 1000)
    return

def ape_rest():
    print("APE Rest")
    # winsound.Beep(600, 1000)
    for i in range(apec_rest):
        t.sleep(1)
    # winsound.Beep(440, 1000)
    return

def c_phase():
    print("C")
    winsound.Beep(600, 1000)
    for i in range(corrective):
        t.sleep(1)
    winsound.Beep(440, 1000)
    return

def rest_phase():
    for i in range(rest):
        t.sleep(1)
    return

if __name__== "__main__":
    for i in range(circuits):

        for j in range(3):
            ape_phase()
            if j == 2:
                break
            ape_rest()

        rest_phase()
        for j in range(4):
            c_phase
        rest_phase()

    print("Time is up")
