import typing

from rpg.character.hp_bar import HpMpBar
from rpg.item import weapon_sheet
from rpg.item.weapon import Weapon
from rpg.util.format_color import Color

if typing.TYPE_CHECKING:
    from rpg.item.item import ConsumableItem, KeyItem


class Character:
    def __init__(self,
                 name: str,
                 hp: int,
                 mp: int
                 ) -> None:
        # object level variables
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.mp = mp
        self.mp_max = mp

        # give a character an inventory
        self.consumables: list['ConsumableItem'] = []
        self.key_items: list['KeyItem'] = []

        self.weapon = weapon_sheet.fists

    def add_consumable(self, item: 'ConsumableItem', amount: int):
        for existing_item in self.consumables:
            if existing_item.name == item.name:
                existing_item.amount += amount
                if amount > 0:
                    print(f"Received {item.name} x{amount}!")
                else:
                    print(f"Lost {amount}x {item.name}!")
                return
        if amount > 0:
            item.amount = amount
            self.consumables.append(item)
            print(f"Received {item.name} x{amount}!")

    def use_consumable(self, index: int):
        if index < 0 or index >= len(self.consumables):
            return False
        self.consumables[index].consume_item(self)
        self.consumables[index].amount -= 1
        if self.consumables[index].amount <= 0:
            del self.consumables[index]
        return True

    # basically INVENTORY
    # bc we want to print consumable items in fights, not key items
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
                 mp: int,
                 ) -> None:
        super().__init__(name, hp, mp)

        self.default_weapon = self.weapon
        self.hp_bar = HpMpBar(self, hp_color=Color.GREEN, mp_color=Color.BLUE)

    def equip(self, weapon: Weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")


class Enemy(Character):
    def __init__(self,
                 name: str,
                 hp: int,
                 mp: int,
                 weapon: Weapon,
                 ) -> None:
        super().__init__(name, hp, mp)
        # Enemy only has one weapon so it does not need equip method
        self.weapon = weapon

        self.hp_bar = HpMpBar(self, hp_color=Color.RED, mp_color=Color.MAGENTA)
