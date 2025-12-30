import time

minutes = 2
for x in range(minutes):
    secondes = 60
    for x in range(secondes):
        if secondes >= 0: 
            time.sleep(0.1)
            print(f"{secondes - 1}")
            secondes -= 1