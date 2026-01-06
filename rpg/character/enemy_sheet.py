from rpg.item import item_sheet
from rpg.item.item_sheet import mega_ether, mega_potion, elixir, hi_ether, hi_potion, robot_chip, crab_shell, \
    gorilla_paw, ether
from rpg.item.weapon_sheet import iron_sword, fists, robot_claw, dagger, pincers, mystery_sword

from rpg.character.character import Enemy
from rpg.magic import magic_sheet

ferry_man: Enemy = Enemy("Ferryman", 50, 50, "neutral", fists, [ether], 100)
ferry_man.set_stats(5,5,5,5,5,5)

### mystery man is demo enemy in chuck mode ###
mystery_man: Enemy = Enemy("Mystery Man", 200, 200, "neutral",
                           mystery_sword, [mega_potion, mega_ether, elixir], 1000)
mystery_man.add_consumable(item_sheet.mega_potion, 1, False)
mystery_man.add_consumable(item_sheet.mega_ether, 1, False)
mystery_man.add_consumable(item_sheet.elixir, 1, False)
mystery_man.learn_spell(magic_sheet.blizzard, False)
mystery_man.learn_spell(magic_sheet.fire, False)
mystery_man.learn_spell(magic_sheet.thunder, False)
mystery_man.learn_spell(magic_sheet.aero, False)
mystery_man.learn_spell(magic_sheet.water, False)
mystery_man.learn_spell(magic_sheet.flare, False)
mystery_man.learn_spell(magic_sheet.cure, False)
mystery_man.set_stats(10, 10, 10, 10, 10, 10)

gambler: Enemy = Enemy("Gambler", 30, 20, "wind", dagger, [hi_potion], 250)
gambler.learn_spell(magic_sheet.aero, False)
gambler.add_consumable(item_sheet.hi_potion, 1, False)
gambler.set_stats(5, 5, 5, 5, 5, 5)

robot_bellboy: Enemy = Enemy("Robot Bellboy", 100,0,"lightning", robot_claw, [robot_chip], 500)
robot_bellboy.set_stats(10, 20, 0, 0, 10, 0)

huge_crab: Enemy = Enemy("Huge Crab", 60, 60, "water", pincers, [crab_shell], 500)
huge_crab.learn_spell(magic_sheet.water, False)
huge_crab.learn_spell(magic_sheet.blizzara, False)
huge_crab.set_stats(10, 10, 20, 20, 10, 10)


gorilla: Enemy = Enemy("Gorilla", 150, 150, "neutral", fists, [gorilla_paw, mega_potion], 750)
gorilla.learn_spell(magic_sheet.fira, False)
gorilla.learn_spell(magic_sheet.aerora, False)
gorilla.learn_spell(magic_sheet.cura, False)
gorilla.add_consumable(item_sheet.mega_potion, 1, False)
gorilla.set_stats(30, 20, 10, 10, 5, 5)


### ARENA ENEMIES
## contest 1
#arena_enemy1: