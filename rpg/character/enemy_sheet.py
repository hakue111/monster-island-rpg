from rpg.item.weapon_sheet import iron_sword, fists, robot_claw, dagger, pincers, mystery_sword

from rpg.character.character import Enemy
from rpg.magic import magic_sheet

ferry_man: Enemy = Enemy("Ferryman", 50, 50, "neutral", fists)
ferry_man.learn_spell(magic_sheet.ice)
ferry_man.learn_spell(magic_sheet.fire)
ferry_man.learn_spell(magic_sheet.lightning)
ferry_man.learn_spell(magic_sheet.wind)
ferry_man.learn_spell(magic_sheet.water)

mystery_man: Enemy = Enemy("Mystery Man", 100, 100, "neutral", mystery_sword)
mystery_man.learn_spell(magic_sheet.flare)
mystery_man.learn_spell(magic_sheet.cure)

gambler: Enemy = Enemy("Gambler", 30, 20, "wind", dagger)
gambler.learn_spell(magic_sheet.wind)

robot_bellboy: Enemy = Enemy("Robot Bellboy", 200,0,"lightning", robot_claw)
#drops robot chip

huge_crab: Enemy = Enemy("Huge Crab", 50, 25, "ice", pincers)
huge_crab.learn_spell(magic_sheet.water)
huge_crab.learn_spell(magic_sheet.ice)
#drops crab shell

gorilla: Enemy = Enemy("Gorilla", 60, 60, "neutral", fists)
gorilla.learn_spell(magic_sheet.fire)
gorilla.learn_spell(magic_sheet.cure)
#drops gorilla fist