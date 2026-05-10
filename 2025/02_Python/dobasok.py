import random

def kozte(szam, also, felso):
    if also < szam < felso:
        return True
    else:
        return False
dobasok_szama = 150
talalat = 0
for i in range(150):
    dobas = random.randint(1,12)
    if kozte(dobas, 4, 8):
        talalat += 1
szazalek = (talalat / dobasok_szama) * 100
print(f"A  {dobasok_szama} dobásból {talalat} esett 4 es 8 koze")
print(f"Ez az osszes dobas {szazalek:.2f} százaléka")

