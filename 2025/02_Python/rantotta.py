import math

vendegek = int(input("Add meg a mai vendégek számát:"))
tojasok_rakt = int(input( "Add meg a tojások számát raktáron:"))

need_egg = math.ceil((vendegek * 3) * 1.1)
print(f"Ennyi vendéghez ennyi tgojás kell: {need_egg}")
kell_meg = need_egg - tojasok_rakt
print(f"Ennyi tojás kell még: {kell_meg}")


