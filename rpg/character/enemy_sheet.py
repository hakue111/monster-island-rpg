from rpg.item.weapon_sheet import iron_sword, fists, robot_claw, dagger, pincers, mystery_sword

from rpg.character.character import Enemy

ferry_man: Enemy = Enemy("Ferryman", 25, 10, "neutral", fists)
mystery_man: Enemy = Enemy("Mystery Man", 80, 100, "neutral", mystery_sword)
gambler: Enemy = Enemy("Gambler", 30, 20, "wind", dagger)
robot_bellboy: Enemy = Enemy("Robot Bellboy", 200,0,"lightning", robot_claw)
huge_crab: Enemy = Enemy("Huge Crab", 50, 25, "ice", pincers)