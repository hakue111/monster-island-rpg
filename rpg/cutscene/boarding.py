import random
from time import sleep

from rpg.character.enemy_sheet import ferry_man
from rpg.cutscene.cutscene import Cutscene
from rpg.game import Game
from rpg.item import item_sheet, weapon_sheet
from rpg.item.weapon import Weapon
from rpg.item.weapon_sheet import iron_sword, short_bow, dagger
from rpg.magic import magic_sheet
from rpg.util.clear_screen import clear_screen
from rpg.character.battle_scene import start_battle, Outcome


def chuck_mode(game: Game):
    print("+++INITIATING TEST MODE+++")
    game.hero.learn_spell(magic_sheet.ice, False)
    game.hero.learn_spell(magic_sheet.fire, False)
    game.hero.learn_spell(magic_sheet.lightning, False)
    game.hero.learn_spell(magic_sheet.wind, False)
    game.hero.learn_spell(magic_sheet.water, False)
    game.hero.learn_spell(magic_sheet.darkness, False)
    game.hero.learn_spell(magic_sheet.flare, False)
    game.hero.learn_spell(magic_sheet.cure, False)
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

    game.hero.add_key_item(item_sheet.robot_chip,1, False)




class BoardingScene(Cutscene):
    starter_weapons: list[Weapon] = [iron_sword, short_bow, dagger]
    def run(self, game: Game):
        clear_screen()
        print("You are about to take the ferry to MONSTER ISLAND.")
        print("Ferryman: What is your name?")

        name_choice = input("> ")
        game.hero.name = name_choice.strip()


        # TEST/CHEAT MODE "CHUCK"
        if game.hero.name.casefold().strip() == "chuck":
            chuck_mode(game)
            return


        print(f"Ferryman: So, you are {game.hero.name}? Please board the ferry. We are departing soon.")
        sleep(1)
        print("You will need a proper weapon. Choose yours:")
        self.pick_weapon(game)
        sleep(2)
        print("The ferryman lays out five books in front of you.")
        sleep(2)
        print("Ferryman: 'It's time you learn your first MAGIC spell.'")
        sleep(2)
        print("'Which of these spells do you wish to learn?'")
        sleep(2)
        self.choose_magic(game)
        sleep(2)
        print("By the way, you will need a few healing items!")
        game.hero.add_consumable(item_sheet.potion, 5, True)

        sleep(2)

        print(f"{game.hero.name} boards the Ferry.")
        sleep(2)
        print(f"The Ferry horn honks and the ship departs. Soon, the mainland will be out of sight.")
        self.ferry_waiting(game)
        print()
        sleep(2)
        if game.choices["ferryman_dead"]:
            print("You arrive on Monster Island")
            sleep(2)
            print("You are greeted by the Mystery Man.")
            sleep(2)
            print("Mystery Man: 'What do we have here?\nDid you experience shipwreck?")
            user_choice = input("Tell him the truth about what you did to the ferryman?\n1: Truth\n2: Lie\n> ")
            if user_choice == "1":
                print("Mystery Man: 'Haha that's pretty ballsy. Hats off.'")
                sleep(2)
                print("You are some evil motherfucker. You will feel right at home here.")
                sleep(2)
                print("'You truly deserve a fitting MAGIC spell!")
                game.hero.learn_spell(magic_sheet.darkness, True)
                game.hero.elemental = "darkness"
                print("Mystery Man: 'Also, your elemental will change to DARKNESS!")
                sleep(2)
                print("'Enjoy your new power.'")
            if user_choice == "2":
                print("Come on, no need to lie. I know what you did. I don't care.")
                sleep(2)
                print("But know this: Monster Island won't be as easy as killing the Ferryman ;) .")
        else:
            print("You arrive on Monster Island. You are greeted by the Mystery Man.")
            print(f"Mystery Man: Welcome to Monster Island, {game.hero.name}. Enjoy your stay...")
            sleep(2)

    def choose_magic(self, game: Game):
        elemental_info = "'This will also be your own elemental from now on.\nIf elemental and spell match, the spells becomes twice as strong!'"
        print(f"1: Ice \n2: Fire \n3: Lightning\n4: Wind\n5: Water")
        user_choice = input("> ")
        if user_choice == "1":
            print("Ferryman: 'You shall now be able to cast ICE MAGIC!'")
            print(elemental_info)
            game.hero.learn_spell(magic_sheet.ice, True)
            game.hero.elemental = "ice"
            return
        if user_choice == "2":
            print("Ferryman: 'You shall now be able to cast FIRE MAGIC!'")
            print(elemental_info)
            game.hero.learn_spell(magic_sheet.fire, True)
            game.hero.elemental = "fire"
            return
        if user_choice == "3":
            print("Ferryman: 'You shall now be able to cast LIGHTNING MAGIC!'")
            print(elemental_info)
            game.hero.learn_spell(magic_sheet.lightning, True)
            return
        if user_choice == "4":
            print("Ferryman: 'You shall now be able to cast WIND MAGIC!")
            print(elemental_info)
            game.hero.learn_spell(magic_sheet.wind, True)
            game.hero.elemental = "wind"
            return
        if user_choice == "5":
            print("Ferryman: 'You shall now be able to cast WATER MAGIC!")
            print(elemental_info)
            game.hero.learn_spell(magic_sheet.water, True)
            game.hero.elemental = "water"
            return
        else:
            print(
            "Alright, if you don't want to answer, you won't learn any spells. Tough luck.")

    def pick_weapon(self, game: Game):
        print(f"1: Iron Sword\n2: Short Bow\n3: Dagger")
        user_choice = input("> ")
        if user_choice == "1":
            print("Ferryman: 'An excellent choice!'")
            game.hero.equip(weapon_sheet.iron_sword, True)
            self.starter_weapons.remove(iron_sword)
            return
        if user_choice == "2":
            print("Ferryman: 'A clever choice!'")
            game.hero.equip(weapon_sheet.short_bow, True)
            self.starter_weapons.remove(short_bow)
            return
        if user_choice == "3":
            print("Ferryman: 'A dangerous choice! Oh well, you do you!'")
            game.hero.equip(weapon_sheet.dagger, True)
            self.starter_weapons.remove(dagger)
            return
        print(f"If you don't want to choose a weapon, you won't get any. Tough luck.")


    def ferry_waiting(self, game: Game):
        print(f"With your weapon and magic spell equipped, you are waiting for the ferry to reach the island.")
        print(f"However, this might still take a little while.")
        sleep(1)
        print("What do you want to do until then?")
        sleep(1)
        print(f"1: Talk to the ferryman\n2: Sleep\n3: Attack the ferryman")
        user_choice = input("> ")
        if user_choice == "1":
            print("It's going to take a while before we reach Monster Island.")
            print("You better get some rest.")
        if user_choice == "2":
            print(f"{game.hero.name} takes a nap...")
            sleep(1)
            print("Zzzz....")
            sleep(1)
            print("Zzzz....")
            sleep(1)
            print("Zzzz....")
            sleep(1)
            print("The ferry has arrived on the island!")
        if user_choice == "3":
            print(f"What the fuck are you doing, {game.hero.name}?!")
            ferry_man.equip(self.starter_weapons[random.randrange(0, len(self.starter_weapons)-1)])
            win = start_battle(game.hero, ferry_man, True)
            if win == Outcome.WIN:
                game.choices["ferryman_dead"] = True
                print("The Ferryman dies and the ferry sinks.")
                sleep(2)
                print("However, you hold onto driftwood.")
                sleep(2)
                print("The currents wash you ashore on MONSTER ISLAND.")
            elif win == Outcome.LOSS:
                sleep(2)
                print("You die.")
                sleep(2)
                print("The ferryman throws your corpse aboard.")
                sleep(2)
                print("You fucking dumbass.")
                clear_screen()
                exit()




