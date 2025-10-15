import typing

if typing.TYPE_CHECKING:
    from rpg.character.character import Character


class Magic:
    def __init__(self,
                 name: str,
                 elemental: str,
                 mp_cost: int
                 ):
        self.name = name
        self.elemental = elemental
        self.mp_cost = mp_cost

    def cast_magic(self, caster: 'Character', target: 'Character'):
        raise NotImplementedError()


class WhiteMagic(Magic):
    def __init__(self,
                 name: str,
                 elemental: str,
                 mp_cost: int,
                 heal: int
                 ):
        super().__init__(name, elemental, mp_cost)
        self.heal = heal

    def cast_magic(self, caster: 'Character', target: 'Character'):
        if caster.mp < 0:
            print(f"{caster.name} does not have enough MP to cast {self.name}!")
        else:
            caster.mp -= self.mp_cost
            caster.hp += self.heal
            if caster.hp > caster.hp_max:
                caster.hp = caster.hp_max
            print(f"Restored {self.heal} HP!")


class BlackMagic(Magic):
    def __init__(self,
                 name: str,
                 elemental: str,
                 mp_cost: int,
                 dmg: int
                 ):
        super().__init__(name, elemental, mp_cost)
        self.dmg = dmg


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


    def cast_magic(self, caster: 'Character', target: 'Character'):
        if caster.mp < self.mp_cost:
            print(f"{caster.name} does not have enough MP to cast {self.name}!")
            return False
        else:
            target.hp -= self.dmg * self.weakness(target)
            caster.mp -= self.mp_cost
            print(f"{caster.name} casts {self.name} onto {target.name}")
            return True


