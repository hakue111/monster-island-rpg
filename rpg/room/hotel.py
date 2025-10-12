from rpg.character import enemy_sheet
from rpg.character.battle_scene import start_battle
from rpg.character.outcome import Outcome
from rpg.game import Game
from rpg.room.room import Room
from rpg.room.roomobject import RoomObject

# first we define the object that is present and interactable in the room:
class RobotBellboy(RoomObject):
    LOOK = "Look at the ROBOT BELLBOY"
    TALK = "Talk to the ROBOT BELLBOY"
    FIGHT = "Attack the ROBOT BELLBOY"

# constructor for interactions with said object:
    def __init__(self):
        self.interactions = [
            RobotBellboy.LOOK,
            RobotBellboy.TALK,
            RobotBellboy.FIGHT,
        ]
# method for interaction with said object:
    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == RobotBellboy.TALK:
            self.talk(game, room)
        elif interaction == RobotBellboy.LOOK:
            print("As you try to muster the mysterious man, he pulls his hat further down into his face.")
        elif interaction == RobotBellboy.FIGHT:
            self.fight(game, room)

# method for talking to said object:
    def talk(self, game: Game, room: Room):
        print("Robot Bellboy: Welcome to the Monster Island Grand Hotel.")
        print("What can I do for you?")

# method for fighting said object:
    def fight(self, game: Game, room: Room):
        result = start_battle(game.hero, enemy_sheet.robot_bellboy)
        if result == Outcome.WIN:
            print("The Mystery Man died...or did he?")
            room.objects.remove(self)
        elif result == Outcome.LOSS:
            print("You died (lol). Game Over!")
            exit()

# define a door to return to another room:
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

