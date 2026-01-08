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
from rpg.character.enemy_randgen import randenemy_gen
from rpg.room.arena_contests import *
from rpg.room.arena_contests import contest_gen


# first we define the object that is present and interactable in the room:
class ArenaReceptionist(RoomObject):
    TALK = "Talk to the ARENA Receptionist"

# constructor for interactions with said object:
    def __init__(self):
        self.interactions = [
            ArenaReceptionist.TALK,
        ]
# method for interaction with said object:
    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == ArenaReceptionist.TALK:
            self.talk(game, room)

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
                    print_ws("Receptionist: 'The ARENA is a place to fight.\n Winning gives you experience and items.'")
                elif index == 2:
                    print_ws("Every contest consists of 5 battles.")
                    print_ws("You have to win all 5 fights in a row to get the prize!")
                    print_ws("Losing will not kill you. If you lose, your HP and MP will be fully restored.")
                elif index == 3:
                    print_ws("Which tier do you want to fight?")
                    print_ws("1: [TIER I]")
                    print_ws("2: [TIER II]'")
                    print_ws("3: '[TIER III]")
                    user_input = input("> ")
                    if user_input.strip() == "1":
                        self.arena_fight(game, room, 1)
                    elif user_input.strip() == "2":
                        self.arena_fight(game, room, 2)
                    elif user_input.strip() == "3":
                        self.arena_fight(game, room, 3)
                    else:
                        print("Invalid choice.")
                    return
                elif index == 4:
                    return
            except ValueError:
                print(f"Input '{user_input}' is not a valid choice!")

    def arena_fight(self, game: Game, room: Room, tier: int):
        arena_enemy = contest_gen(tier)
        for enemy in arena_enemy:
            result = start_battle(game.hero, enemy, True)
            if result == Outcome.WIN:
                print_ws("You win!")
            elif result == Outcome.LOSS:
                print_ws("You lost!")
                break
                print_ws()









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
class Arena(Room):
    def __init__(self):
        self.objects = [
            ArenaReceptionist(),
        ]

    def describe(self, game: Game):
        print("You are at the ARENA.")

