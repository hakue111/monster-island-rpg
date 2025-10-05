from character_tutorial import *
from weapon import *

hero = Hero(name = "Hero", hp = 30)
hero.equip(iron_sword)
enemy = Enemy(name = "Enemy", hp = 30, weapon = short_bow)

hero.hp_bar.draw()
enemy.hp_bar.draw()
while True:
    hero.attack(enemy)
    enemy.attack(hero)
    hero.hp_bar.draw()
    enemy.hp_bar.draw()

    hero.drop()

    input("> ")



