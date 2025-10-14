class Magic:
    def __init__(self,
                 name: str,
                 elemental: str,
                 dmg: int,
                 mp_cost: int,
                 ):
        self.name = name
        self.elemental = elemental
        self.dmg = dmg
        self.mp_cost = mp_cost



    def weakness(self):
        if self.elemental == "fire":

