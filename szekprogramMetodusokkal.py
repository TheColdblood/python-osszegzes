from Szek import Szek

def pldlistaban():
    peldany1 = Szek("kék", 3)
    peldany2 = Szek("piros", 4)
    peldany3 = Szek("zöld", 5)

    szekek = [peldany1, peldany2, peldany3]
    return szekek


def listaki(lista):
    for index in range(0, len(lista), 1):
        print(lista[index])

#rovid verzio
#listaki(pldlistaban())

#hosszu verzio
#szekLista = pldlistaban()
#listaki(szekLista)


def osszegzes(szekek):
    print("Összesen hány székláb van a teremben?")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labakszama
    print(f"{ossz} db")


def maximum(szekek):
    maxIndex = 0
    for index in range(0, len(szekek), 1):
        if szekek[index].labakszama > szekek[maxIndex].labakszama:
            maxIndex = index
    print(f"A legtöbb lábbal rendelkező szék színe: {szekek[maxIndex].szin}")


def megszamlalas(szekek):
    print("Hány 4-nél több lábú szék van: ", end="")
    db = 0
    for index in range(0, len(szekek), 1):
        if szekek[index].labakszama > 4:
            db += 1
    print(f"{db} db")


def eldontes(szekek):
    vanE = False
    print("Van-e piros, négy lábú szék: ",end="")
    for index in range(0, len(szekek), 1):
        if szekek[index].szin == str("piros") and szekek[index].labakszama == 4:
            vanE = True

    if vanE == True:
        print("Van")
    else:
        print("Nincs")


szekLista = pldlistaban()
listaki(szekLista)
osszegzes(szekLista)
maximum(szekLista)
megszamlalas(szekLista)
eldontes(szekLista)


