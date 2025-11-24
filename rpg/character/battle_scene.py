import random
from time import sleep

from rpg.character.character import Hero, Enemy
from rpg.character.outcome import Outcome
from rpg.item.item import Item, ConsumableItem, KeyItem
from rpg.util.clear_screen import clear_screen


def start_battle(hero: Hero, enemy: Enemy, print_msg: bool) -> Outcome:
    clear_screen()
    sleep(1)
    if print_msg:
        clear_screen()
        print("BATTLE START!")
        sleep(0.5)
        print()
        sleep(0.5)
        print(f"{hero.name} vs {enemy.name}")
        sleep(0.5)
        print()
        sleep(0.5)
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
            sleep(1)
            print(f"{enemy.name} is defeated!")
            sleep(1)
            if enemy.loot:
                for item in enemy.loot:
                    if isinstance(item, ConsumableItem):
                        hero.add_consumable(item, 1, True)
                    elif isinstance(item, KeyItem):
                        hero.add_key_item(item, 1, True)
                    else:
                        raise Exception("Unknown item type")
                    sleep(0.5)

            return Outcome.WIN


def fight(hero: Hero, enemy: Enemy, skip_player: bool):
    if not skip_player:
        hero.attack(enemy)
    if not enemy.is_dead():
        enemy_skip = False
        if enemy.hp / enemy.hp_max <= 0.5:
            for index in range(len(enemy.consumables)):
                if "Potion" in enemy.consumables[index].name:
                    enemy.use_consumable(index)
                    enemy_skip = True
                    break
        if enemy.mp_max > 0 and enemy.mp / enemy.mp_max <= 0.5:
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
    print()
    enemy.hp_bar.draw()
