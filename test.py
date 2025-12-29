import time

minutes = 3
for x in range(minutes):
    secondes = 60
    if secondes >= 0: 
        time.sleep(1)
        print(f"{secondes - 1}")