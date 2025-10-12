from rpg.item.weapons import iron_sword, fists, robot_claw

from rpg.character.character import Enemy

mystery_man: Enemy = Enemy("Mystery Man", 80, iron_sword)
gambler: Enemy = Enemy("Gambler", 30, fists)
robot_bellboy: Enemy = Enemy("Robot Bellboy", 1000, robot_claw)
