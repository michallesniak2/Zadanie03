imie = input("Jak masz na imię? ")
nazwisko = input("Jak masz na nazwisko? ")
wiek = int(input("Ile masz lat? "))

if wiek >= 18:
    odp_1_1 = input("Pijesz (y/n)? ")
    print(odp_1_1)
    odp_1_2 = input("Palisz (y/n)? ")
    print(odp_1_2)
    print(imie,nazwisko,"lat",wiek,"pije",odp_1_1,"pali",odp_1_2)
else:
    odp_2_1 = input("Dobrze się uczysz? (y/n) ")
    print(odp_2_1)
    odp_2_2 = input("Chcesz cukierka? (y/n) ")
    print(odp_2_2)
