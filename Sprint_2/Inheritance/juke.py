import time

energy = 100

door_open = False

if door_open is False:
    while energy >= 0:
        time.sleep(2)
        energy -= 1
        print(energy)
else:
    print(energy)