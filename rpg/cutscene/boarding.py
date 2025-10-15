from time import sleep

from rpg.cutscene.cutscene import Cutscene
from rpg.game import Game
from rpg.item import item_sheet, weapon_sheet
from rpg.magic import magic_sheet
from rpg.util.clear_screen import clear_screen


class BoardingScene(Cutscene):
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

        self.fav_color(game)

        game.hero.add_consumable(item_sheet.potion, 5)

        sleep(2)

        print(f"{game.hero.name} boards the Ferry.")
        sleep(1)
        print(f"The Ferry horn honks and the ship departs. Soon, the mainland will be out of sight.")
        print(f"{game.hero.name}, you are going on a dark and mysterious adventure. Be careful...")
        print()
        sleep(2)
        print("You arrive on Monster Island. You are greeted by the Mystery Man.")
        print(f"Mystery Man: Welcome to Monster Island, {game.hero.name}. Enjoy your stay...")
        sleep(1)

    def fav_color(self, game: Game):
        print(f"1: Light Blue\n2: Red \n3: Yellow\n4: Green\n5: Dark Blue")
        user_choice = input("> ")
        if user_choice == "1":
            print("Ferryman: 'You shall now be able to cast ICE MAGIC!'")
            game.hero.learn_spell(magic_sheet.ice)
            return
        if user_choice == "2":
            print("Ferryman: 'You shall now be able to cast FIRE MAGIC!'")
            game.hero.learn_spell(magic_sheet.fire)
            return
        if user_choice == "3":
            print("Ferryman: 'You shall now be able to cast LIGHTNING MAGIC!'")
            game.hero.learn_spell(magic_sheet.lightning)
            return
        if user_choice == "4":
            print("Ferryman: 'You shall now be able to cast WIND MAGIC!")
            game.hero.learn_spell(magic_sheet.wind)
            return
        if user_choice == "5":
            print("Ferryman: 'You shall now be able to cast WATER MAGIC!")
            game.hero.learn_spell(magic_sheet.water)
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
            return
        if user_choice == "2":
            print("Ferryman: 'A clever choice!'")
            game.hero.equip(weapon_sheet.short_bow)
            return
        if user_choice == "3":
            print("Ferryman: 'A dangerous choice! Oh well, you do you!'")
            game.hero.equip(weapon_sheet.dagger)
            return
        print(f"You have to pick one, do you really think you can kill those monster on MONSTER ISLAND with your fists??! DUMBASS")
        self.pick_weapon(game)