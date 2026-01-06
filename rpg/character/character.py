import random
import typing
from time import sleep
from typing import Optional

from rpg.character.hp_mp_bar import HpMpBar
from rpg.item import weapon_sheet
from rpg.item.weapon import Weapon
from rpg.magic.magic import Magic
from rpg.util.format_color import Color
from rpg.util.icons import ELEMENTAL_ICONS

if typing.TYPE_CHECKING:
    from rpg.item.item import ConsumableItem, KeyItem, Item
    from rpg.item.weapon import Weapon


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

        self.stat_atk: int = 10
        # used for dealing physical damage

        self.stat_def: int = 10
        # used for taking physical damage

        self.stat_matk: int = 10
        # used for dealing magical damage

        self.stat_mdef: int = 10
        # used for taking magical damage

        self.stat_acc: int = 90
        # used for determining if attack/magic will land

        self.stat_eva: int = 10
        # used for determining if attack/magic will land

        # self.stat_speed: int = 1
        # used for turn order


        # give a character an inventory
        self.consumables: list['ConsumableItem'] = []
        self.key_items: list['KeyItem'] = []
        self.weapons: list['Weapon'] = []
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


    def set_stats(self, stat_atk: int, stat_def: int, stat_matk: int, stat_mdef: int, stat_acc: int, stat_eva: int) -> None:
        if stat_atk > -1:
            self.stat_atk = stat_atk
        if stat_def > -1:
            self.stat_def = stat_def
        if stat_matk > -1:
            self.stat_matk = stat_matk
        if stat_mdef > -1:
            self.stat_mdef = stat_mdef
        if stat_acc > -1:
            self.stat_acc = stat_acc
        if stat_eva > -1:
            self.stat_eva = stat_eva



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

    def print_consumables(self):
        print("Inventory: ")
        for index in range(len(self.consumables)):
            item = self.consumables[index]
            print(f"{index + 1}: {item.name} x{item.amount} - {item.description}.")

    # basically INVENTORY
    # bc we want to print consumable items in fights, not key items
    def choose_consumable(self, print_msg: bool = False):
        self.print_consumables()
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

    def print_spells(self):
        print("Magic Spells: ")
        for index in range(len(self.spells)):
            spell = self.spells[index]
            print(f"{index + 1}: {spell.name}")

    def choose_spell(self, target: 'Character'):
        self.print_spells()
        print("[index] to cast spell or type 'back'.")
        spell = self._choose_spell(self.spells)
        if spell is None:
            return False
        return self.cast_magic(target, spell)


    def attack(self, target) -> None:
        line = (80 * "-")
        battle_rng = random.randrange(0, 100)
        if battle_rng > self.stat_acc - target.stat_eva:
            print(f"{self.name}'s attack missed!")
            return
        critical_hit: bool = battle_rng <= 15
        actual_dmg: int = self.weapon.dmg + self.stat_atk - target.stat_def
        if actual_dmg < 0:
            actual_dmg = 0
        if critical_hit:
            actual_dmg *= 2
        target.hp -= actual_dmg
        target.hp = max(target.hp, 0)
        target.hp_bar.update()
        sleep(0.5)
        if critical_hit:
            print(line)
            print("Critical Hit!!")
            print(f"{self.name} dealt {actual_dmg} damage to {target.name} with {self.weapon.name}!")
            print(line)
            sleep(1)
        else:
            print(line)
            print(f"{self.name} dealt {actual_dmg} damage to {target.name} with {self.weapon.name}!")
            print(line)
            sleep(1)


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
            if print_msg:
                print(f"Received {item.name} x{amount}!")



    def key_item_check(self, key_item: 'KeyItem'):
        for item in self.key_items:
            if item.name == key_item.name:
                return True
        return False

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}', hp={self.hp}, mp={self.mp}, elemental={self.elemental})"

    def __repr__(self):
        return self.__str__()


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

    def add_weapon(self, weapon: Weapon, print_msg: bool) -> None:
        self.weapons.append(weapon)
        if print_msg:
            print(f"{self.name} put {weapon.name} into Inventory.")


    def player_menu(self):
        line = (80 * "-")
        print(line)
        print(f"Player: {self.name}")
        print()
        print(f"💚 HP: {self.hp}/{self.hp_max}")
        print(f"🪄 MP: {self.mp}/{self.mp_max}")
        print()
        print(f"{ELEMENTAL_ICONS[self.elemental]} Elemental: {self.elemental}")
        print()
        print(f"🗡️ Equipped weapon: {self.weapon.name}")
        print()
        key_items = [key_item.name for key_item in self.key_items]
        print(f"🔑 Key Items: {", ".join(key_items)}")
        print()
        print(f"🏺 Consumable Items: ")
        self.choose_consumable()

    #def gain_xp



class Enemy(Character):
    def __init__(self,
                 name: str,
                 hp: int,
                 mp: int,
                 elemental: str,
                 weapon: Weapon,
                 loot: list['Item'] = [],
                 xp_drop: int = 10,
                 tier: int = 1
                 ) -> None:
        super().__init__(name, hp, mp, elemental)
        # Enemy only has one weapon so it does not need equip method
        self.weapon = weapon
        self.loot = loot
        self.xp_drop = xp_drop
        self.tier = tier
        self.hp_bar = HpMpBar(self, hp_color=Color.RED, mp_color=Color.MAGENTA)



    def equip(self, weapon: Weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")
