#megszamlalas
def ketjegyuparos():
    db = 0

    for i in range(10, 100, 1):
        if i % 2 == 0:
            db += 1
    print(db)


#minimum kiválasztás
def nullaig():
    VEGE = 0
    db = 0
    min = 2147483647
    while (szam := int(input("N="))) != VEGE:
        if szam < min:
            min = szam
        db += 1

    print(f"{db} számból a legkisebb: {min}")


nullaig()
