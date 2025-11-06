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


class BoardingScene(Cutscene):
    starter_weapons: list[Weapon] = [iron_sword, short_bow, dagger]
    def run(self, game: Game):
        clear_screen()
        print("One day, as you open your mail, you find a MYSTERIOUS ENVELOPE")
        print("The letter inside proudly proclaims that you've won a free vacation on MONSTER ISLAND")
        print()
        sleep(1)
        print("That's curious, you think to yourself, you don't remember playing the lottery...")
        print()
        sleep(1)
        print("The next morning.")
        print("You are standing on the docks.")
        print("With your baggage and your ticket in your hands, you are about to board the ferry.")
        sleep(1)
        print("Ferryman: What is your name?")

        name_choice = input("> ")
        game.hero.name = name_choice.strip()

        print(f"Ferryman: So, you are {game.hero.name}? Please board the ferry. We are departing soon.")
        sleep(2)
        print("Monster Island is too dangerous without a proper weapon. Choose yours:")
        self.pick_weapon(game)
        sleep(2)
        print("By the way, which of these colors do you like the most?")

        self.choose_elemental(game)

        game.hero.add_consumable(item_sheet.potion, 5)

        sleep(2)

        print(f"{game.hero.name} boards the Ferry.")
        sleep(1)
        print(f"The Ferry horn honks and the ship departs. Soon, the mainland will be out of sight.")
        self.boredom(game)
        print()
        sleep(2)
        print("You arrive on Monster Island. You are greeted by the Mystery Man.")
        print(f"Mystery Man: Welcome to Monster Island, {game.hero.name}. Enjoy your stay...")
        sleep(1)

    def choose_elemental(self, game: Game):
        print(f"1: Light Blue\n2: Red \n3: Yellow\n4: Green\n5: Dark Blue")
        user_choice = input("> ")
        if user_choice == "1":
            print("Ferryman: 'You shall now be able to cast ICE MAGIC!'")
            game.hero.learn_spell(magic_sheet.ice, True)
            game.hero.elemental = "ice"
            return
        if user_choice == "2":
            print("Ferryman: 'You shall now be able to cast FIRE MAGIC!'")
            game.hero.learn_spell(magic_sheet.fire, True)
            game.hero.elemental = "fire"
            return
        if user_choice == "3":
            print("Ferryman: 'You shall now be able to cast LIGHTNING MAGIC!'")
            game.hero.learn_spell(magic_sheet.lightning, True)
            return
        if user_choice == "4":
            print("Ferryman: 'You shall now be able to cast WIND MAGIC!")
            game.hero.learn_spell(magic_sheet.wind, True)
            game.hero.elemental = "wind"
            return
        if user_choice == "5":
            print("Ferryman: 'You shall now be able to cast WATER MAGIC!")
            game.hero.learn_spell(magic_sheet.water, True)
            game.hero.elemental = "water"
            return
        else:
            print(
            "Come on now, this ain't hard to answer. Just pick a color you like.")

    def pick_weapon(self, game: Game):
        print(f"1: Iron Sword\n2: Short Bow\n3: Dagger")
        user_choice = input("> ")
        if user_choice == "1":
            print("Ferryman: 'An excellent choice!'")
            game.hero.equip(weapon_sheet.iron_sword)
            self.starter_weapons.remove(iron_sword)
            return
        if user_choice == "2":
            print("Ferryman: 'A clever choice!'")
            game.hero.equip(weapon_sheet.short_bow)
            self.starter_weapons.remove(short_bow)
            return
        if user_choice == "3":
            print("Ferryman: 'A dangerous choice! Oh well, you do you!'")
            game.hero.equip(weapon_sheet.dagger)
            self.starter_weapons.remove(dagger)
            return
        print(f"You have to pick one, do you really think you can kill those monster on MONSTER ISLAND with your fists??! DUMBASS")
        self.pick_weapon(game)


    def boredom(self, game: Game):
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
            sleep(3)
            print("Zzzz....")
            sleep(2)
            print("Zzzz....")
            sleep(1)
            print("Zzzz....")
            sleep(3)
            print("The ferry has arrived on the island!")
        if user_choice == "3":
            print(f"What the fuck are you doing, {game.hero.name}?!")
            ferry_man.equip(self.starter_weapons[random.randrange(0, len(self.starter_weapons)-1)])
            win = start_battle(game.hero, ferry_man)
            if win == Outcome.WIN:
                print(f"Ferryman: {game.hero.name} what the FUCK HAVE YOU DONE?!")
                sleep(1)
                print("Ferryman: Now were are both going to die!")
                sleep(1)
                print("The Ferryman dies and the ferry sinks.")
                sleep(1)
                print("You drown. Well done, dumbass!")
                sleep(2)
                print("GAME OVER")
                exit()




