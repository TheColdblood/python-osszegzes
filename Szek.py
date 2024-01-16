class Szek:
    def __init__(self, szin: str, labakszama: int):
        self.szin = szin
        self.labakszama = labakszama

    def __str__(self):
        return (f"szín:{self.szin} lábak száma: {self.labakszama}")