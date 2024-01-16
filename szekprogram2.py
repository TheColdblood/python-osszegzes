def szekInit(szin: str, labszam: int):
    print(f"Szín: {szin} Lábszám: {labszam}")


szekInit("kék", 3)
szekInit("piros", 4)
szekInit("zöld", 5)


def szekStr(szin: str, labszam: int):
    return (f"Szín: {szin} Lábszám: {labszam}")

print(szekStr("kék", 3))
