from rpg.character import enemy_sheet
from rpg.character.battle_scene import start_battle
from rpg.character.outcome import Outcome
from rpg.game import Game
from rpg.item.item_sheet import robot_chip, crab_shell
from rpg.room.room import Room
from rpg.room.roomobject import RoomObject

# first we define the object that is present and interactable in the room:
class HugeCrab(RoomObject):
    LOOK = "Look at the HUGE CRAB"
    TALK = "Talk to the HUGE CRAB"
    FIGHT = "Attack the HUGE CRAB"

# constructor for interactions with said object:
    def __init__(self):
        self.interactions = [
            HugeCrab.LOOK,
            HugeCrab.TALK,
            HugeCrab.FIGHT,
        ]
# method for interaction with said object:
    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == HugeCrab.TALK:
            self.talk(game, room)
        elif interaction == HugeCrab.LOOK:
            print("A huge crab. It's fucking huge. Jesus fucking Christ.")
        elif interaction == HugeCrab.FIGHT:
            self.fight(game, room)

# method for talking to said object:
    def talk(self, game: Game, room: Room):
        print("You're talking to the huge crab.")
        sleep(1)
        print("...")
        sleep(1)
        print("The crab doesn't say anything. It's a crab, dumbass.")
        return None

# method for fighting said object:
    def fight(self, game: Game, room: Room):
        result = start_battle(game.hero, enemy_sheet.robot_bellboy)
        if result == Outcome.WIN:
            print("The Crab died and falls apart...")
            room.objects.remove(self)
            game.hero.key_items.append(crab_shell)
            print(f"{game.hero.name} picked up a mysterious CRAB SHELL.")
        elif result == Outcome.LOSS:
            print("You died. Game Over!")
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
            HugeCrab(),
            DoorIslandDocks(),
        ]

    def describe(self, game: Game):
        print("You are at the beach.")

