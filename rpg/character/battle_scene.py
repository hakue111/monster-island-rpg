import random

from rpg.character.character import Hero, Enemy
from rpg.character.outcome import Outcome
from rpg.item import item
from rpg.util.clear_screen import clear_screen


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
                item_used = hero.print_consumables(True)
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
    enemy_skip = False
    if enemy.hp / enemy.hp_max <= 0.5:
        for index in range(len(enemy.consumables)):
            if "Potion" in enemy.consumables[index].name:
                enemy.use_consumable(index)
                enemy_skip = True
                break
    if enemy.mp / enemy.mp_max <= 0.5:
        for index in range(len(enemy.consumables)):
            if "Ether" in enemy.consumables[index].name:
                enemy.use_consumable(index)
                enemy_skip = True
                break
    if not enemy_skip:
        enemy_randomness = random.randrange(0,100)
        spell = random.choice(enemy.spells) if enemy.spells else None
        if enemy_randomness >= 70 and spell is not None and enemy.mp >= spell.mp_cost:
            enemy.cast_magic(hero, spell)
        else:
            enemy.attack(hero)
    hero.hp_bar.draw()
    enemy.hp_bar.draw()
