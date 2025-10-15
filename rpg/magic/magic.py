from rpg.character.character import Character


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



    def weakness(self, target):
        if self.elemental == "ice" and target.elemental == "fire":
            return 2
        elif self.elemental == "fire" and target.elemental == "ice":
            return 2
        elif self.elemental == "lightning" and target.elemental == "wind":
            return 2
        elif self.elemental == "wind" and target.elemental == "lightning":
            return 2
        elif self.elemental == "water" and target.elemental == "fire":
            return 2
        elif self.elemental == "lightning" and target.elemental == "water":
            return 2
        elif self.elemental == "ice" and target.elemental == "ice":
            return 0.5
        elif self.elemental == "fire" and target.elemental == "fire":
            return 0.5
        elif self.elemental == "lightning" and target.elemental == "lightning":
            return 0.5
        elif self.elemental == "wind" and target.elemental == "wind":
            return 0.5
        elif self.elemental == "water" and target.elemental == "water":
            return 0.5
        else:
            return 1


    def cast_magic(self, caster: Character, target: Character):
        if self.mp < self.mp_cost:
            print(f"{caster.name} does not have enough MP to cast {self.name}!")
            return False
        else:
            target.hp -= self.dmg * self.weakness(target)
            self.mp -= self.mp_cost
            print(f"{caster.name} casts {self.name} onto {target.name}")
            return True


