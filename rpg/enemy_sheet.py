from rpg.character import Enemy
from rpg.weapon import iron_sword, fists, robot_claw

mystery_man: Enemy = Enemy("Mystery Man", 80, iron_sword)
gambler: Enemy = Enemy("Gambler", 30, fists)
robot_bellboy: Enemy = Enemy("Robot Bellboy", 1000, robot_claw)
