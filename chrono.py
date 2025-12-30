import time

def AffichageSS(minutes):
    secondes = 60
    for x in range(secondes):
        if secondes >= 0: 
            time.sleep(0.1)
            secondes -= 1


def AffichageMM(minutes):
    for x in range(minutes):
        if minutes >=0:
            AffichageSS(minutes)
            minutes -= 1


AffichageMM(2)