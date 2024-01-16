from Szek import Szek

peldany1 = Szek("kék", 3)
peldany2 = Szek("piros", 4)
peldany3 = Szek("zöld", 5)

print(peldany1.__str__())
print(peldany2)
print(peldany3)

szekek = [peldany1, peldany2, peldany3]

def labakSzama():
    print("Összesen hány székláb van a teremben?")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labakszama
    print(f"{ossz} db")

labakSzama()

def maxLabSzin():
    maxndex = 0
    for index in range(0, len(szekek), 1):
        if szekek[index] > szekek[maxIndex]:
            maxIndex = index
    print(f"A legtöbb lábbal rendelkező szék színe: {szekek[maxIndex].szin}")
maxLabSzin()