from time import sleep

from rpg.character import enemy_sheet
from rpg.character.battle_scene import start_battle
from rpg.character.outcome import Outcome
from rpg.game import Game
from rpg.item import item_sheet
from rpg.item.item_sheet import robot_chip
from rpg.magic import magic_sheet
from rpg.room.room import Room
from rpg.room.roomobject import RoomObject
from rpg.util import helpers
from rpg.util.helpers import print_ws


# first we define the object that is present and interactable in the room:
class ArenaReceptionist(RoomObject):
    TALK = "Talk to the ARENA Receptionist"
    #REGISTER = "Register for the ARENA Challenge"
    FIGHT = "Attack the ARENA Receptionist."

# constructor for interactions with said object:
    def __init__(self):
        self.interactions = [
            ArenaReceptionist.TALK,
            ArenaReceptionist.FIGHT
        ]
# method for interaction with said object:
    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == ArenaReceptionist.TALK:
            self.talk(game, room)
        elif interaction == ArenaReceptionist.FIGHT:
            self.fight(game, room)

    def talk(self, game: Game, room: Room):
        print_ws("Welcome to the Monster Island ARENA.")
        print_ws("What can I do for you?")

        while True:
            print("1: 'What is this place?'")
            print("2: 'Explain the ARENA rules.'")
            print("3: 'REGISTER for the ARENA CHALLENGE")
            print("4: 'Sorry, I've got to go.' [LEAVE]")
            user_input = input("> ")
            try:
                index = int(user_input)
                if index == 1:
                    print_ws("Receptionist: 'The ARENA is a place to fight. Winning gives you experience and items.'")
                elif index == 2:
                    print_ws("Every contest consists of 5 battles.")
                    #write the contests
                    print_ws("You will randomly receive HP or MP restores after every battle.")
                    #write method for random hp/mp restore
                    print_ws("Losing will not kill you. If you lose, your HP and MP will be fully restored")
                elif index == 3:
                    print("Which list do you want to fight?")
                    #write method for arena list selection
                    self.fight(game, room)
                    return
                elif index == 4:
                    return
            except ValueError:
                print(f"Input '{user_input}' is not a valid choice!")


    def fight(self, game: Game, room: Room):
        result = start_battle(game.hero, en True)
        if result == Outcome.WIN:
            print_ws()
            room.objects.remove(self)
            room.objects.append(HotelCounter())
        elif result == Outcome.LOSS:
            print_ws("You lost!")
            exit()




class HotelCounter(RoomObject):
    LOOK = "Look behind the COUNTER"

    used: bool

    def __init__(self):
        self.used = False
        self.interactions = [
            HotelCounter.LOOK,
        ]

    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == HotelCounter.LOOK:
            if self.used:
                print("There's nothing here.")
            else:
                print("Behind the counter, you find a yellow book.")
                user_input = input("Pick up the book? (yes/no)\n> ")
                if user_input.casefold().strip() == "yes":
                    if not game.hero.has_spell(magic_sheet.lightning.name):
                        print("As you touch the yellow book, you gain the power of Lightning!")
                        sleep(0.5)
                        game.hero.learn_spell(magic_sheet.lightning, True)

                    elif game.hero.has_spell(magic_sheet.lightning.name):
                        print("As you touch the yellow book, your power of Lightning becomes stronger!")
                        sleep(0.5)
                        game.hero.learn_spell(magic_sheet.lightning_2, True)

                    elif game.hero.has_spell(magic_sheet.lightning_2.name):
                        print("As you touch the yellow book, your power of Lightning becomes stronger!")
                        game.hero.learn_spell(magic_sheet.lightning_3, True)

                    elif game.hero.has_spell(magic_sheet.lightning_3.name):
                        print("As you touch the yellow book...nothing happens.")
                    self.used = True
                else:
                    print("You decide to not touch the book.")








class DoorIslandDocks(RoomObject):
    GOTO = "Return to the ISLAND DOCKS"

# constructor for said door:
    def __init__(self):
        self.interactions = [
            DoorIslandDocks.GOTO
        ]
# method for interacting with said door/room:
    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == DoorIslandDocks.GOTO:
            print("You're walking back towards the docks.")
            game.select_room("island_docks")

# now we define the actual room we're in:
class Hotel(Room):
    def __init__(self):
        self.objects = [
            RobotBellboy(),
            DoorIslandDocks(),
        ]

    def describe(self, game: Game):
        print("You are at the hotel")

