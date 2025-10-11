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
        print(f"Mystery Man: Welcome to Monster Island, {name_choice}. Enjoy your stay...")

        print("Where do you wish to go now?")
        while True:
            user_input = input("1: Gambler Stand (North)\n2: Beach (East)\n3: Ferry (South)\n4: Hotel (West)\n5: Stay at the docks and talk to the Mystery Man\n> ")
            try:
                index = int(user_input)
                if index == 1:
                    print(f"{name_choice} goes to the Gambler Stand in the North.")
                    GamblerRoom().gambler_scene()
                elif index == 2:
                    print(f"{name_choice} goes to the Beach in the East.")
                    BeachRoom().beach_scene()
                elif index == 3:
                    print(f"{name_choice} goes to the Ferry in the South.")
                    FerryRoom().ferry_scene()
                elif index == 4:
                    print(f"{name_choice} goes to the Hotel in the West.")
                    HotelRoom().hotel_scene()
                elif index == 5:
                    print(f"{name_choice} decides to stay at the docks and talk to the Mystery Man.")
                    self.talk_mysteryman()
            except ValueError:
                print(f"Input '{user_input}' not a valid choice!")


    def talk_mysteryman(self):
        print("You are talking to the Mystery Man.")
        input("Press Enter to continue...")
        print(f"So, {character.player.name}, what do you want to know?")
        while True:
            user_input = input(
                "1: 'What is this place?'\n2: 'How can I leave?'\n3: 'Why did you pick that awkward name, Mystery Man? Are you stupid?'\n> ")
            try:
                index = int(user_input)
                if index == 1:
                    print(f"Mystery Man: 'What do you think MONSTER ISLAND means, dumbass?")
                elif index == 2:
                    print(f"You can try to leave if you want...")
                elif index == 3:
                    print(f"I'm going to teach you some manners, you little bastard!")
                    self.fight_mysteryman()
            except ValueError:
                print(f"Input '{user_input}' not a valid choice!")






        #while True:
            #choice = input("Please enter where you want to go (Hotel/Gambler Stand/Beach)\n>")
            #if choice.casefold().strip() == "Hotel".casefold():
              #print(f"{name_choice} goes to the Hotel.")
                #hotel()
            #elif choice.casefold().strip() == "Gambler Stand".casefold():
                #print(f"{name_choice} goes to the Gambler Stand.")
                #GamblerRoom().gambler_stand()
            #elif choice.casefold().strip() == "Beach".casefold():
                #print(f"{name_choice} goes to the Forest")
                #forest()
            #else:
                #print("Invalid input. Please input Hotel/Gambler Stand/Forest and press Enter")

    def fight_mysteryman(self):
        result = start_battle(character.player, self.mystery_man)
        if result == "win":
            print("The Mystery Man died...or did he?")
            # how does game return to room selection after this?
        elif result == "lose":
            print("You died (lol). Game Over!")
            exit

