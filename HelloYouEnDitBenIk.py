import datetime
import time

def helloyou():
    x = datetime.datetime.now()
    print("Hello you, ik ben Sem Hiel " + x.strftime("| %c"))
    time.sleep(2)
    print("Wie ben jij?")
    time.sleep(1)
    n = input('Naam: ')
    time.sleep(1)
    print("Hallo, " + n + " Aangenaam.")
    print("Hoe oud ben je?")
    leeftijd = input()
    print("Leuk! Je bent dus", leeftijd, ". Ik ben 17 jaar!")
    time.sleep(1)
    print("Waar woon je?")
    woonplaats = input()
    print("Leuk! Ik woon in Purmerend.")
    time.sleep(1)
    print("Wil je dit programma herhalen?")
    herhalen = input().lower()
    if herhalen == "ja":
        return helloyou()
    elif herhalen == "nee":
        print("Het programma word nu afgesloten.")
    else:
        print("Geen geldige input!")
        print("Het programma word nu afgesloten.")

helloyou()
