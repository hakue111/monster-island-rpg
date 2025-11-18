import typing
from typing import Optional

from rpg.character.hp_mp_bar import HpMpBar
from rpg.item import weapon_sheet
from rpg.item.weapon import Weapon
from rpg.magic.magic import Magic
from rpg.util.format_color import Color

if typing.TYPE_CHECKING:
    from rpg.item.item import ConsumableItem, KeyItem


class Character:
    def __init__(self,
                 name: str,
                 hp: int,
                 mp: int,
                 elemental: str
                 ) -> None:
        # object level variables
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.mp = mp
        self.mp_max = mp
        self.elemental = elemental
        self.spells: list[Magic] = []

        # give a character an inventory
        self.consumables: list['ConsumableItem'] = []
        self.key_items: list['KeyItem'] = []

        self.weapon = weapon_sheet.fists
    # give a character the ability to learn magic spells
    def learn_spell(self, magic: Magic, print_msg: bool) -> None:
        self.spells.append(magic)
        if print_msg:
            print(f"{self.name} learned {magic.name}!")


    def has_spell(self, spell_name: str) -> bool:
        for spell in self.spells:
            if spell.name == spell_name:
                return True
        return False


    def add_consumable(self, item: 'ConsumableItem', amount: int, print_msg: bool):
        for existing_item in self.consumables:
            if existing_item.name == item.name:
                existing_item.amount += amount
                if amount > 0 and print_msg:
                    print(f"Received {item.name} x{amount}!")
                elif print_msg:
                    print(f"Lost {amount}x {item.name}!")
                return
        if amount > 0:
            item.amount = amount
            self.consumables.append(item)
            if print_msg:
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
    def print_consumables(self, print_msg: bool):
        print("Inventory: ")
        for index in range(len(self.consumables)):
            item = self.consumables[index]
            print(f"{index + 1}: {item.name} x{item.amount} - {item.description}.")
        user_input = input("[index] to use item or back.\n> ")
        if user_input.casefold().strip() == "back":
            return False
        try:
            index = int(user_input)
            return self.use_consumable(index - 1)
        except ValueError:
            print("Invalid index. No item found.")
            return False

    def _choose_spell(self, options: list[Magic]) -> Optional[Magic]:
        while True:
            try:
                text = input("> ")
                if text.casefold().strip() == "back":
                    return None
                choice = int(text)
                return options[choice - 1]
            except Exception:
                print("Invalid choice.")
                return None


    def print_spells(self, target: 'Character'):
        print("Magic Spells: ")
        for index in range(len(self.spells)):
            spell = self.spells[index]
            print(f"{index + 1}: {spell.name}")
        print("[index] to cast spell or back.")
        spell = self._choose_spell(self.spells)
        if spell is None:
            return False
        return self.cast_magic(target, spell)


    def attack(self, target) -> None:
        target.hp -= self.weapon.dmg
        target.hp = max(target.hp, 0)
        target.hp_bar.update()
        print(f"{self.name} dealt {self.weapon.dmg} damage to {target.name} with {self.weapon.name}")


    def cast_magic(self, target: 'Character', spell: 'Magic'):
        if spell not in self.spells:
            return False
        spell.cast_magic(self, target)
        return True


    def is_dead(self):
        return self.hp <= 0

    def add_key_item(self, item: 'KeyItem', amount: int, print_msg: bool):
        for existing_item in self.key_items:
            if existing_item.name == item.name:
                existing_item.amount += amount
                if amount > 0 and print_msg:
                    print(f"Received {item.name} x{amount}!")
                else:
                    print(f"Lost {amount}x {item.name}!")
                return
        if amount > 0:
            item.amount = amount
            self.key_items.append(item)
            print(f"Received {item.name} x{amount}!")



    def key_item_check(self, key_item: 'KeyItem'):
        for item in self.key_items:
            if item.name == key_item.name:
                return True
        return False


class Hero(Character):
    def __init__(self,
                 name: str,
                 hp: int,
                 mp: int,
                 elemental: str
                 ) -> None:
        super().__init__(name, hp, mp, elemental)

        self.default_weapon = self.weapon
        self.hp_bar = HpMpBar(self, hp_color=Color.GREEN, mp_color=Color.BLUE)

    def equip(self, weapon: Weapon, print_msg: bool) -> None:
        self.weapon = weapon
        if print_msg:
            print(f"{self.name} equipped a(n) {self.weapon.name}!")


class Enemy(Character):
    def __init__(self,
                 name: str,
                 hp: int,
                 mp: int,
                 elemental: str,
                 weapon: Weapon,
                 ) -> None:
        super().__init__(name, hp, mp, elemental)
        # Enemy only has one weapon so it does not need equip method
        self.weapon = weapon

        self.hp_bar = HpMpBar(self, hp_color=Color.RED, mp_color=Color.MAGENTA)

    def equip(self, weapon: Weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")