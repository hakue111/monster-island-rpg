from typing import Callable

from rpg import character
from rpg.battle_scene import start_battle
from rpg.character import Enemy
from rpg.item import Item


class SceneOption:
    def play(self):
        raise NotImplementedError()


class SceneOptionDialogue(SceneOption):
    def __init__(self, dialogue: str):
        self.dialogue = dialogue

    def play(self):
        print(f"{self.dialogue}")


class SceneOptionItem(SceneOption):
    def __init__(self, item: Item, item_amount: int):
        self.item = item
        self.item_amount = item_amount

    def play(self):
        character.player.add_consumable(self.item, self.item_amount)


class SceneOptionFight(SceneOption):
    def __init__(self, enemy: Enemy):
        self.enemy = enemy

    def play(self):
        start_battle(character.player, self.enemy)


class SceneOptionLambda(SceneOption):
    def __init__(self, func: Callable):
        self.func = func

    def play(self):
        self.func()


class Scene:
    name: str
    key: str
    scene_option: list[SceneOption]

    def __init__(self, name: str, key: str):
        self.name = name
        self.key = key
        self.scene_option: list[SceneOption] = []

    def add_option(self, option: SceneOption):
        self.scene_option.append(option)

    def play_scene(self):
        for option in self.scene_option:
            option.play()
            input("Press enter to continue...")
