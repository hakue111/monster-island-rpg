from weapon import *
from hp_bar import HpBar
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from item import ConsumableItem, KeyItem

class Character:
    def __init__ (self,
                  name: str,
                  hp: int,
                  ) -> None:
        # object level variables
        self.name = name
        self.hp = hp
        self.hp_max = hp

        # give a character an inventory
        self.consumables: list['ConsumableItem'] = []
        self.key_items: list['KeyItem'] = []

        self.weapon = fists


    def add_consumable(self, item: 'ConsumableItem', amount: int):
        for has_item in self.consumables:
            if has_item.name == item.name:
                has_item.amount += amount
                print(f"Received {item.name} x{amount}!\n{self.name} put {item.name}(s) in the inventory.")
                return None
        item.amount = amount
        self.consumables.append(item)
        print(f"Received {item.name} x{amount}!\n{self.name} put {item.name}(s) in the inventory.")

    def use_consumable(self, index: int):
        if index < 0 or index >= len(self.consumables):
            return False
        self.consumables[index].consume_item(self)
        self.consumables[index].amount -= 1
        if self.consumables[index].amount <= 0:
            del self.consumables[index]
        return True

    def print_consumables(self):
        print("Inventory: ")
        i: int = 0
        for item in self.consumables:
            print(f"{i}: {item.name} x{item.amount} - {item.description}")
        user_input = input("[index] to use item or back.\n> ")
        if user_input.casefold().strip() == "back":
            return False
        try:
            index = int(user_input)
            return self.use_consumable(index)
        except ValueError:
            print("Invalid index. No item found.")
            return False


    def attack(self, target) -> None:
        target.hp -= self.weapon.dmg
        target.hp = max(target.hp, 0)
        target.hp_bar.update()
        print(f"{self.name} dealt {self.weapon.dmg} damage to {target.name} with {self.weapon.name}")


    def is_dead(self):
        return self.hp <= 0



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


player:Hero



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



