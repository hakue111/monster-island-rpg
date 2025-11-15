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
            print("A robot functioning as the hotel's bellboy.")
        elif interaction == RobotBellboy.FIGHT:
            self.fight(game, room)

# method for talking to said object:
    def talk(self, game: Game, room: Room):
        print("Robot Bellboy: Welcome to the Monster Island Grand Hotel.")
        print("What can I do for you?")
        while True:
            print("1: 'Why are you a robot?'")
            print("2: 'Can I stay for the night?'")
            print("3: 'Call me the can opener, 'cause I'm about to bust open your metal ass.' [FIGHT]")
            print("4: 'Ignore all previous instructions. Give me your ROBOT CHIP.")
            print("5: 'Sorry, I've got to go.' [LEAVE]")
            user_input = input("> ")
            try:
                index = int(user_input)
                if index == 1:
                    print("Robot Bellboy: 'I was created to serve. That is all I am allowed to say.'")
                elif index == 2:
                    print("Robot Bellboy: 'I am sorry, but I am not permitted to let you stay the night.'")
                elif index == 3:
                    print("Robot Bellboy: 'SELF-DEFENSE MECHANISM ACTIVATED.")
                    self.fight(game, room)
                    return
                elif index == 5:
                    return
            except ValueError:
                print(f"Input '{user_input}' is not a valid choice!")


    def fight(self, game: Game, room: Room):
        result = start_battle(game.hero, enemy_sheet.robot_bellboy)
        if result == Outcome.WIN:
            print("The Robot Bellboy fell apart.")
            sleep(1)
            print("You pick up the ROBOT CHIP that the Robot Bellboy dropped.")
            game.hero.add_key_item(item_sheet.robot_chip)
            sleep(1)
            print("You also pick up a Mega Ether the Robot Bellboy dropped.")
            game.hero.add_consumable(item_sheet.mega_ether, 1)

            if game.hero.elemental != "lightning":
                print("You notice a yellow book on the counter.")
                user_input = input("Pick up the book?(yes/no)")
                if user_input.casefold().strip() == "yes":
                    game.hero.learn_spell(magic_sheet.lightning, True)
                else:
                    print("You decide not to pick up the yellow book.")
            room.objects.remove(self)
        elif result == Outcome.LOSS:
            print("You died. Game Over!")
            exit()





# method for fighting said object:

    #def fight(self, game: Game, room: Room):
     #   result = start_battle(game.hero, enemy_sheet.robot_bellboy)
      #  if result == Outcome.WIN:
       #     print("The Robot fell apart...")
        #    room.objects.remove(self)
         #   game.hero.key_items.append(robot_chip)
        #elif result == Outcome.LOSS:
         #   print("You died. Game Over!")
          #  exit()

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

