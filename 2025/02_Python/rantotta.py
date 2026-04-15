vendegek = int(input("Add meg a mai vendégek számát:"))
tojasok_rakt = (input( "Add meg a tojások számát raktáron:"))
vendegek_szama = vendegek
tojasok_szama = tojasok_rakt
need_egg = vendegek_szama * 3,1
print(f"Ennyi vendéghez ennyi tgojás kell: {need_egg}")
if need_egg < tojasok_szama:
    print("Kell még tojást venni")

else: 
    print("Van elég tojás")


