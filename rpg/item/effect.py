from typing import TYPE_CHECKING

from rpg import item
from rpg.item import item_sheet
from rpg.item.item import ConsumableItem

if TYPE_CHECKING:
    from rpg.character.character import Character, Hero


class Effect:
    def apply_effect(self, character: 'Character', item: 'ConsumableItem'):
        raise NotImplementedError

    #def __str__(self):
        #return f"Consumable Item(name='{self.character}', description={self.description}, amount={self.amount}, effects={self.effects})"

    #def __repr__(self):
        #return self.__str__()


class RestoreHPEffect(Effect):
    def __init__(self, restore: int):
        self.restore = restore

    def apply_effect(self, character: 'Character', item: 'ConsumableItem'):
        character.hp += self.restore
        if character.hp > character.hp_max:
            character.hp = character.hp_max
        print(f"{character.name} restored {self.restore} HP with {item.name}!")


class RestoreMPEffect(Effect):
    def __init__(self, restore: int):
        self.restore = restore

    def apply_effect(self, character: 'Character', item: 'ConsumableItem'):
        character.mp += self.restore
        if character.mp > character.mp_max:
            character.mp = character.mp_max
        print(f"{character.name} restored {self.restore} MP with {item.name}!")