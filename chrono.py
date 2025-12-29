import time

def compteur(minutes):
    for x in range(minutes):
        secondes = 60
        if secondes >= 0:
            time.sleep(1)
            print(f"{secondes - 1}")

compteur(5)