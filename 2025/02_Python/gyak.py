class Urhajosok:
    def __init__(self, nev,  orszag, nem, szulev, urido):
        self.nev = nev
        self.orszag = orszag
        self.nem = nem
        self.szulev = int(szulev)
        self.urido = int(urido)


urhajosok = []
fajl = open("2025/02_Python/urhajos.txt", "r", encoding="utf8")
fajl.readline()

for sor in fajl:
    adatok = sor.strip().split(";")

    uj = Urhajosok(
        adatok[0],
        adatok[1] ,       
        adatok[2]  ,      
        adatok[3]   ,     
        adatok[4]    ,    
    )     

    urhajosok.append(uj)

fajl.close()

#3.4 feladat

print(f"Ennyi urhajos van a fájlban : {len(urhajosok)}")

#3.5 feladat

van = False

for u in urhajosok:
    if u.orszag == "ITA":
        van = True
if van:
    print("Van olasz szarmazasu az urhajosok kozott")

else:
    print("Nincxs olasz")

#3.6 feladat
osszeg = 0
darab = 0

for u in urhajosok:
    if u.nem == "N":
        osszeg += u.urido
        darab += 1

atlag = osszeg/darab

print(f"A női űrhajósok átlagosan {atlag:.2f} időt töltenek az űrben")


#3.7 feladat
legfiatalabb = urhajosok[0]

for u in urhajosok:
    if u.szulev > legfiatalabb.szulev:
        legfiatalabb = u
print("Legfiatalabb urhajos: ")
print("Neve:", legfiatalabb.nev)
print("Orszaga:", legfiatalabb.orszag)
print("Neme:", legfiatalabb.nem)
print("Szulev:", legfiatalabb.szulev)
print("Urido:", legfiatalabb.urido)

