from rpg.character.character import Hero, Enemy
from rpg.character.outcome import Outcome
from rpg.item import weapon_sheet
from rpg.util.clear_screen import clear_screen
import random


def start_battle(hero: Hero, enemy: Enemy) -> Outcome:
    clear_screen()
    hero.hp_bar.draw()
    enemy.hp_bar.draw()
    while True:
        user_input = input("1: Attack | 2: Magic | 3: Inventory\n> ")
        try:
            index = int(user_input)
            if index == 1:
                fight(hero, enemy, False)
            elif index == 2:
                spell_used = hero.print_spells(enemy)
                if spell_used:
                    fight(hero, enemy, True)
            elif index == 3:
                item_used = hero.print_consumables()
                if item_used:
                    fight(hero, enemy, True)
        except ValueError:
            print(f"Input '{user_input}' not a valid choice!")

        if hero.is_dead():
            print("You lose! Game Over!")
            return Outcome.LOSS
        elif enemy.is_dead():
            print(f"{enemy.name} is defeated!")
            return Outcome.WIN


def fight(hero: Hero, enemy: Enemy, skip_player: bool):
    if not skip_player:
        hero.attack(enemy)
        enemy_randomness = random.randrange(0,100)
        if enemy_randomness <= 79:
            enemy.attack(hero)
        else:
            enemy.cast_magic(hero, enemy.spells[random.choice(enemy.spells)])
    hero.hp_bar.draw()
    enemy.hp_bar.draw()
