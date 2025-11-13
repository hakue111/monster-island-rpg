import typing

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


    def print_spells(self, target: 'Character'):
        print("Magic Spells: ")
        i: int = 0
        for spell in self.spells:
            print(f"{i}: {spell.name}")
        user_input = input("[index] to cast spell or back.\n> ")
        if user_input.casefold().strip() == "back":
            return False
        try:
            index = int(user_input)
            # Return the spell bc it tells us if we could cast it or did not have enough mp
            return self.cast_magic(target, index)
        except ValueError:
            print("Invalid index. No Magic Spell found.")
            return False



    def attack(self, target) -> None:
        target.hp -= self.weapon.dmg
        target.hp = max(target.hp, 0)
        target.hp_bar.update()
        print(f"{self.name} dealt {self.weapon.dmg} damage to {target.name} with {self.weapon.name}")


    def cast_magic(self, target: 'Character', spell_index: int):
        if spell_index < 0 or spell_index >= len(self.spells):
            return False
        else:
            self.spells[spell_index].cast_magic(self, target)
            return True


    def is_dead(self):
        return self.hp <= 0

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

    def equip(self, weapon: Weapon) -> None:
        self.weapon = weapon
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