from Szek import Szek

peldany1 = Szek("kék", 3)
peldany2 = Szek("piros", 4)
peldany3 = Szek("zöld", 5)
peldany4 = Szek("sárga", 6)


print(peldany1.__str__())
print(peldany2)
print(peldany3)


szekek = [peldany1, peldany2, peldany3, peldany4]


def labakSzama():
    #összegzés
    print("Összesen hány székláb van a teremben?")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labakszama
    print(f"{ossz} db")
labakSzama()



def maxLabSzin():
    #maximum
    maxIndex = 0
    for index in range(0, len(szekek), 1):
        if szekek[index].labakszama > szekek[maxIndex].labakszama:
            maxIndex = index
    print(f"A legtöbb lábbal rendelkező szék színe: {szekek[maxIndex].szin}")
maxLabSzin()



def negynelTobb():
    #megszamlalas
    print("Hány 4-nél több lábú szék van: ", end="")
    db = 0
    for index in range(0, len(szekek), 1):
        if szekek[index].labakszama > 4:
            db += 1
    print(f"{db} db")
negynelTobb()

def vanePirosNegy():
    #eldöntés
    vanE = False
    print("Van-e piros, négy lábú szék: ",end="")
    for index in range(0, len(szekek), 1):
        if szekek[index].szin == str("piros") and szekek[index].labakszama == 4:
            vanE = True

    if vanE == True:
        print("Van")
    else:
        print("Nincs")
vanePirosNegy()