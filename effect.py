from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from character import Character


class Effect:
    def apply_effect(self, character: 'Character'):
        raise NotImplementedError


class HealEffect(Effect):
    def __init__(self, restore: int):
        self.restore = restore
    def apply_effect(self, character: 'Character'):
        character.hp += self.restore
        if character.hp > character.hp_max:
            character.hp = character.hp_max
        print(f"Restored {self.restore} HP!")