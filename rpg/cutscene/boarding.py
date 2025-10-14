from time import sleep

from rpg.cutscene.cutscene import Cutscene
from rpg.game import Game
from rpg.item import item_sheet, weapon_sheet
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
        sleep(1)
        print(f"Ferryman: By the way, I have something useful for you.")

        game.hero.add_consumable(item_sheet.potion, 5)

        print(f"Ferryman: And take one of these for your journey:")
        self.pick_weapon(game)



        print(f"{game.hero.name} boards the Ferry.")
        sleep(1)
        print(f"The Ferry horn honks and the ship departs. Soon, the mainland will be out of sight.")
        print(f"{game.hero.name}, you are going on a dark and mysterious adventure. Be careful...")
        print()
        sleep(2)
        print("You arrive on Monster Island. You are greeted by the Mystery Man.")
        print(f"Mystery Man: Welcome to Monster Island, {game.hero.name}. Enjoy your stay...")
        sleep(1)


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