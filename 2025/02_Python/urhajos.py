class Urhajos:
    def __init__(self, nev, orszag, nem, szuletesi_ev, urido):
        self.nev = nev
        self.orszag = orszag
        self.nem = nem
        self.szuletesi_ev = int(szuletesi_ev)
        self.urido = int(urido)


# 3. feladat
urhajosok = []

fajl = open(“02_Python\urhajos.txt”, “r”, encoding=“utf-8”)
fajl.readline()  # fejlec atugrasa

for sor in fajl:
    adatok = sor.strip().split(“;”)

    uj = Urhajos(
        adatok[0],
        adatok[1],
        adatok[2],
        adatok[3],
        adatok[4]
    )

    urhajosok.append(uj)

fajl.close()


# 3.4 feladat
print(“3.4. feladat: Az allomanyban”, len(urhajosok), “urhajos adatai talalhatok.”)

# 3.5 feladat
van_olasz = False

for u in urhajosok:
    if u.orszag == “ITA”:
        van_olasz = True

if van_olasz:
    print(“3.5. feladat: Az urhajosok kozott van olasz szarmazasu.”)
else:
    print(“3.5. feladat: Az urhajosok kozott nincs olasz szarmazasu.”)


# 3.6 feladat
osszeg = 0
db = 0

for u in urhajosok:
    if u.nem == “N”:
        osszeg += u.urido
        db += 1

atlag = osszeg / db

print(f”3.6. feladat: A noi urhajosok atlagosan {atlag:.2f} napot toltottek az urben.”)


# 3.7 feladat
legfiatalabb = urhajosok[0]

for u in urhajosok:
    if u.szuletesi_ev > legfiatalabb.szuletesi_ev:
        legfiatalabb = u
print(“3.7. feladat: A legfiatalabb urhajos:”)
print(“    Neve:”, legfiatalabb.nev)
print(“    Orszaga:”, legfiatalabb.orszag)
print(“    Neme:”, legfiatalabb.nem)
print(“    Szuletesi eve:”, legfiatalabb.szuletesi_ev)
print(“    Urben toltott ideje:”, legfiatalabb.urido, “nap”)



