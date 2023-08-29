import time as t
import winsound

# Durations are provided in seconds.
work_duration = 20
rest_duration = 10
work_rounds = 5


def work_phase():
    winsound.Beep(440, 1000)
    print("Switch.")
    for i in range(work_duration):
        t.sleep(1)
    return

def rest_phase():
    winsound.Beep(600, 1000)
    print("Small Rest.")
    for i in range(rest_duration):
        t.sleep(1)
    return

if __name__== "__main__":
    for i in range(3):
        for i in range(work_rounds):
            work_phase()
            rest_phase()
    winsound.Beep(600, 200)
    winsound.Beep(600, 200)
    winsound.Beep(440, 500)
    print("Time is up")
