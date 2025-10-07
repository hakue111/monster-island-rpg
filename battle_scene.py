from typing import Literal

from character import *
from weapon import *

def start_battle(hero, enemy) -> Literal["win", "lose"]:
    hero.equip(iron_sword)
    # hero = Hero(name = "Hero", hp = 30)
    # enemy = Enemy(name = "Enemy", hp = 30, weapon = short_bow)
    hero.hp_bar.draw()
    enemy.hp_bar.draw()
    while True:
        hero.attack(enemy)
        enemy.attack(hero)
        hero.hp_bar.draw()
        enemy.hp_bar.draw()

        if hero.is_dead():
            print("You lose! Game Over!")
            return "lose"
        elif enemy.is_dead():
            print(f"{enemy.name} is defeated!")
            return "win"
        input(">[ Enter ]")



