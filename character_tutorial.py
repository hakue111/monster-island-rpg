from weapon import *
from hp_bar_tutorial import HpBar

class Character:

    def __init__ (self,
                  name: str,
                  hp: int,
                  ) -> None:
    # object level variables
        self.name = name
        self.hp = hp
        self.hp_max = hp

        self.weapon = fists

    def attack(self, target) -> None:
        target.hp -= self.weapon.dmg
        target.hp = max(target.hp, 0)
        target.hp_bar.update()
        print(f"{self.name} dealt {self.weapon.dmg} damage to {target.name} with {self.weapon.name}")


class Hero(Character):
    def __init__(self,
                 name: str,
                 hp: int,
                 ) -> None:
        super().__init__(name = name, hp = hp)

        self.default_weapon = self.weapon
        self.hp_bar = HpBar(self, color = "green")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")


    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon








class Enemy(Character):
    def __init__(self,
                 name: str,
                 hp: int,
                 weapon
                 ) -> None:
        super().__init__(name = name, hp = hp)
    # Enemy only has one weapon so it does not need equip method
        self.weapon = weapon

        self.hp_bar = HpBar(self, color = "red")



