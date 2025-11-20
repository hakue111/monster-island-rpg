from rpg.item import item_sheet
from rpg.item.item_sheet import mega_ether, mega_potion, elixir, hi_ether, hi_potion, robot_chip, crab_shell, \
    gorilla_paw
from rpg.item.weapon_sheet import iron_sword, fists, robot_claw, dagger, pincers, mystery_sword

from rpg.character.character import Enemy
from rpg.magic import magic_sheet

ferry_man: Enemy = Enemy("Ferryman", 50, 50, "neutral", fists)

### mystery man is demo enemy in chuck mode! ###
mystery_man: Enemy = Enemy("Mystery Man", 200, 200, "neutral",
                           mystery_sword, [mega_potion, mega_ether, elixir])
mystery_man.add_consumable(item_sheet.mega_potion, 1, False)
mystery_man.add_consumable(item_sheet.mega_ether, 1, False)
mystery_man.add_consumable(item_sheet.elixir, 1, False)
mystery_man.learn_spell(magic_sheet.ice, False)
mystery_man.learn_spell(magic_sheet.fire, False)
mystery_man.learn_spell(magic_sheet.lightning, False)
mystery_man.learn_spell(magic_sheet.wind, False)
mystery_man.learn_spell(magic_sheet.water, False)
mystery_man.learn_spell(magic_sheet.flare, False)
mystery_man.learn_spell(magic_sheet.cure, False)

gambler: Enemy = Enemy("Gambler", 30, 20, "wind", dagger, [hi_potion])
gambler.learn_spell(magic_sheet.wind, False)
gambler.add_consumable(item_sheet.hi_potion, 1, False)

robot_bellboy: Enemy = Enemy("Robot Bellboy", 100,0,"lightning", robot_claw, [robot_chip])

huge_crab: Enemy = Enemy("Huge Crab", 60, 60, "water", pincers, [crab_shell])
huge_crab.learn_spell(magic_sheet.water, False)
huge_crab.learn_spell(magic_sheet.ice_2, False)

gorilla: Enemy = Enemy("Gorilla", 150, 150, "neutral", fists, [gorilla_paw, mega_potion])
gorilla.learn_spell(magic_sheet.fire_2, False)
gorilla.learn_spell(magic_sheet.wind_2, False)
gorilla.learn_spell(magic_sheet.cure_2, False)
gorilla.add_consumable(item_sheet.mega_potion, 1, False)