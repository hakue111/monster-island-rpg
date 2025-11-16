from typing import TYPE_CHECKING

from rpg import item
from rpg.item import item_sheet
from rpg.item.item import ConsumableItem

if TYPE_CHECKING:
    from rpg.character.character import Character, Hero


class Effect:
    def apply_effect(self, character: 'Character', item: 'ConsumableItem'):
        raise NotImplementedError


class RestoreHPEffect(Effect):
    def __init__(self, restore: int):
        self.restore = restore

    def apply_effect(self, character: 'Character', item: 'ConsumableItem'):
        character.hp += self.restore
        if character.hp > character.hp_max:
            character.hp = character.hp_max
        print(f"Restored {self.restore} HP with {item.name}!")


class RestoreMPEffect(Effect):
    def __init__(self, restore: int):
        self.restore = restore

    def apply_effect(self, character: 'Character', item: 'ConsumableItem'):
        character.mp += self.restore
        if character.mp > character.mp_max:
            character.mp = character.mp_max
        print(f"Restored {self.restore} MP with {item.name}!")