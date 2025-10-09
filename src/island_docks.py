import character
import item_sheet
from battle_scene import start_battle
from character import Enemy, Hero
from gambler_stand import GamblerRoom
from room_state import Room
from weapon import iron_sword


class IslandDocks(Room):
    def __init__(self, name: str,
                 description:str
                 ):
        super().__init__(name, description)
        self.mystery_man: Enemy = Enemy("Mystery Man",100, iron_sword)

    def boarding(self):
        print("You have won a free vacation on Monster Island.")
        print("The name already indicates that this island means danger.")
        input("Press Enter to continue...")
        print("You are standing on the docks. With your baggage and your ticket in your hands, you are about to board the ferry.")
        print("The ferryman checks your ticket.")
        input("Press Enter to continue...")
        print("Ferryman: What is your name?")
        name_choice = input("@Player: Please enter your name and press Enter:\n> ")
        character.player = Hero(name_choice, 100)
        print(f"Ferryman: So, you are {name_choice}? Please board the ferry. We are departing soon.")
        print(f"Ferryman: By the way, I have something useful for you.")
        # give player a potion
        character.player.add_consumable(item_sheet.potion, 5)
        print(f'{name_choice} boards the ferry.')
        print(f"The ferry horn honks and the ship departs. Soon, the mainland will be out of sight.")
        print(f"{name_choice}, you are going on a dark and mysterious adventure. Be careful...")
        input("Press Enter to continue...")

        print("You arrive on Monster Island. You are greeted by the Mystery Man.")
        print(f"Mysterious Man: Welcome to Monster Island, {name_choice}. Enjoy your stay...")
        print("There are three places you can go now: The Hotel, the gambler stand and the Beach. Where do you go?")
        while True:
            choice = input("Please enter where you want to go (Hotel/Gambler Stand/Beach)\n>")
            if choice.casefold().strip() == "Hotel".casefold():
                print(f"{name_choice} goes to the Hotel.")
                hotel()
            elif choice.casefold().strip() == "Gambler Stand".casefold():
                print(f"{name_choice} goes to the Gambler Stand.")
                GamblerRoom().gambler_stand()
            elif choice.casefold().strip() == "Beach".casefold():
                print(f"{name_choice} goes to the Forest")
                forest()
            else:
                print("Invalid input. Please input Hotel/Gambler Stand/Forest and press Enter")

    def mystery_man_fight(self):
        result = start_battle(character.player, self.mystery_man)
        if result == "win":
            print("The Mysterious Man died.")
        elif result == "lose":
            print("You died (lol). Game Over!")
