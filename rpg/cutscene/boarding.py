from time import sleep

from rpg.cutscene.cutscene import Cutscene
from rpg.game import Game
from rpg.item import item_sheet


class BoardingScene(Cutscene):
    def run(self, game: Game):
        print("One day, as you open your mail, you find a MYSTERIOUS ENVELOPE")
        print("The letter inside proudly proclaims that you've won a free vacation on MONSTER ISLAND")
        print()
        sleep(2)
        print("That's curious, you think to yourself, you don't remember playing the lottery...")
        print()
        sleep(2)
        print("The next morning.")
        print("You are standing on the docks.")
        print("With your baggage and your ticket in your hands, you are about to board the ferry.")
        sleep(2)
        print("Ferryman: What is your name?")

        name_choice = input("> ")
        game.hero.name = name_choice.strip()

        print(f"Ferryman: So, you are {game.hero.name}? Please board the ferry. We are departing soon.")
        sleep(1)
        print(f"Ferryman: By the way, I have something useful for you.")

        game.hero.add_consumable(item_sheet.potion, 5)

        print(f"{game.hero.name} boards the Ferry.")
        sleep(1)
        print(f"The Ferry horn honks and the ship departs. Soon, the mainland will be out of sight.")
        print(f"{game.hero.name}, you are going on a dark and mysterious adventure. Be careful...")
        print()
        sleep(2)
        print("You arrive on Monster Island. You are greeted by the Mystery Man.")
        print(f"Mystery Man: Welcome to Monster Island, {game.hero.name}. Enjoy your stay...")
        sleep(2)