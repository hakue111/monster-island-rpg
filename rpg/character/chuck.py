from rpg.game import Game
from rpg.item import weapon_sheet, item_sheet
from rpg.magic import magic_sheet


def chuck_mode(game: Game):
    print("+++INITIATING TEST MODE+++")
    game.hero.learn_spell(magic_sheet.ice, False)
    game.hero.learn_spell(magic_sheet.fire, False)
    game.hero.learn_spell(magic_sheet.lightning, False)
    game.hero.learn_spell(magic_sheet.wind, False)
    game.hero.learn_spell(magic_sheet.water, False)
    game.hero.learn_spell(magic_sheet.flare, False)
    game.hero.learn_spell(magic_sheet.cure, False)
    game.hero.learn_spell(magic_sheet.darkness, False)
    game.hero.elemental = "neutral"

    game.hero.equip(weapon_sheet.chuck_sword, False)
    game.hero.hp_max = 500
    game.hero.hp = 500
    game.hero.mp_max = 500
    game.hero.mp = 500

    game.hero.add_consumable(item_sheet.potion, 5, False)
    game.hero.add_consumable(item_sheet.hi_potion, 5, False)
    game.hero.add_consumable(item_sheet.mega_potion, 5, False)
    game.hero.add_consumable(item_sheet.ether, 5, False)
    game.hero.add_consumable(item_sheet.hi_ether, 5, False)
    game.hero.add_consumable(item_sheet.mega_ether, 5, False)
    game.hero.add_consumable(item_sheet.elixir, 5, False)

    game.hero.set_stats(10, 10, 10, 10, 10, 10)


    #game.hero.add_key_item(item_sheet.robot_chip,1, False)