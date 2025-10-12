from typing import Literal

from rpg.character import *
from rpg.weapon import *


def start_battle(hero: Hero, enemy: Enemy) -> Literal["win", "lose"]:
    hero.equip(iron_sword)
    hero.hp_bar.draw()
    enemy.hp_bar.draw()
    while True:
        user_input = input("1: Attack | 2: Show Inventory\n> ")
        try:
            index = int(user_input)
            if index == 1:
                fight(hero, enemy, False)
            elif index == 2:
                item_used = hero.print_consumables()
                if item_used:
                    fight(hero, enemy, True)
        except ValueError:
            print(f"Input '{user_input}' not a valid choice!")

        if hero.is_dead():
            print("You lose! Game Over!")
            return "lose"
        elif enemy.is_dead():
            print(f"{enemy.name} is defeated!")
            return "win"


def fight(hero: Hero, enemy: Enemy, skip_player: bool):
    if not skip_player:
        hero.attack(enemy)
    enemy.attack(hero)
    hero.hp_bar.draw()
    enemy.hp_bar.draw()
