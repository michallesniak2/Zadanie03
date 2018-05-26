import random

flaga = False
moj_licznik = random.randint(1,100)
print(moj_licznik)
licznik = 0

while flaga == False:
    licznik += 1
    wartosc = int(input("Podaj liczbę od 1 do 100: "))
    if wartosc > moj_licznik:
        print("Liczba za duża")
    elif wartosc < moj_licznik:
        print("Liczba za mała")
    else:
        print("BINGO")
        flaga = True


print("Udało ci się zgadnąć po",licznik,"próbach" )