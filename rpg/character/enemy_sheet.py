from rpg.item.weapon_sheet import iron_sword, fists, robot_claw, dagger, pincers

from rpg.character.character import Enemy

mystery_man: Enemy = Enemy("Mystery Man", 80, 100, iron_sword)
gambler: Enemy = Enemy("Gambler", 30, 20, dagger)
robot_bellboy: Enemy = Enemy("Robot Bellboy", 200,0,robot_claw)
huge_crab: Enemy = Enemy("Huge Crab", 50, 25, pincers)