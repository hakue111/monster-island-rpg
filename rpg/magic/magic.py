import random
import typing
from time import sleep


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
            print(f"{caster.name} restored {self.heal} HP with {self.name}!")


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


    def stab(self, caster: 'Character'):
        if self.elemental == caster.elemental:
            return 2
        else:
            return 1

    def cast_magic(self, caster: 'Character', target: 'Character'):
        line = 80 * "-"
        battle_rng = random.randrange(0,100)
        critical_hit: bool = battle_rng <= 10
        actual_dmg: int = self.dmg * self.weakness(target) * self.stab(caster)

        if caster.mp < self.mp_cost:
            print(f"{caster.name} does not have enough MP to cast {self.name}!")
            return False

        if critical_hit:
            actual_dmg *= 2
            target.hp -= actual_dmg
            print(line)
            print("Critical Hit!!")
            print(f"{caster.name} casts {self.name} onto {target.name} & dealt {actual_dmg} HP damage!")
            print(line)
            sleep(1)
            #target.hp = max(target.hp, 0)
            #target.hp_bar.update()

        else:
            target.hp -= actual_dmg
            caster.mp -= self.mp_cost
            print(line)
            print(f"{caster.name} casts {self.name} onto {target.name} & dealt {actual_dmg} HP damage!")
            return True



class EvilMagic(BlackMagic):
    def __init__(self,
                 name: str,
                 elemental: str,
                 mp_cost: int,
                 dmg: int
                 ):
        super().__init__(name, elemental, mp_cost, dmg)
        self.dmg = dmg

    def cast_magic(self, caster: 'Character', target: 'Character'):
        line = 80 * "-"
        battle_rng = random.randrange(0,100)
        critical_hit: bool = battle_rng <= 10
        actual_dmg: int = self.dmg * self.weakness(target) * self.stab(caster)
        recoil_dmg: int = int(actual_dmg * 0.33)

        if caster.mp < self.mp_cost:
            print(f"{caster.name} does not have enough MP to cast {self.name}!")
            return False

        if critical_hit:
            actual_dmg *= 2
            target.hp -= actual_dmg
            caster.hp -= recoil_dmg * 2
            print(line)
            print("Critical Hit!!")
            sleep(1)
            print(f"{caster.name} casts {self.name} onto {target.name} & dealt {actual_dmg} HP damage!")
            sleep(1)
            print(f"{caster.name} suffered {recoil_dmg} HP recoil damage!")
            print(line)
            sleep(1)

        else:
            target.hp -= actual_dmg
            caster.mp -= self.mp_cost
            caster.hp -= recoil_dmg
            print(line)
            print(f"{caster.name} casts {self.name} onto {target.name} & dealt {actual_dmg} HP damage!")
            sleep(1)
            print(f"{caster.name} suffered {recoil_dmg} HP recoil damage!")
            return True




