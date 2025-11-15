from rpg.character import enemy_sheet
from rpg.character.battle_scene import start_battle
from rpg.character.outcome import Outcome
from rpg.game import Game
from rpg.item import item_sheet
from rpg.room import rooms
from rpg.room.room import Room
from rpg.room.roomobject import RoomObject

class MysteryMan(RoomObject):
    TALK = "Talk to the MYSTERY MAN"
    LOOK = "Look at the MYSTERY MAN"
    CHALLENGE = "Challenge the MYSTERY MAN to a duel"
    asked_leave: bool = False

    def __init__(self):
        self.interactions = [
            MysteryMan.TALK,
            MysteryMan.LOOK,
            MysteryMan.CHALLENGE,
        ]

    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == MysteryMan.TALK:
            self.talk(game, room)
        elif interaction == MysteryMan.LOOK:
            print("As you try to muster the mysterious man, he pulls his hat further down into his face.")
        elif interaction == MysteryMan.CHALLENGE:
            self.fight(game, room)

    def talk(self, game, room):
        print(f"So, {game.hero.name}, what do you want to know?")
        while True:
            print("1: 'What is this place?'")
            print("2: 'How can I leave?'")
            print("3: 'Why did you pick that awkward name, Mystery Man? Are you stupid?'")
            print("4: 'Sorry, I've got to go.' [LEAVE]")
            user_input = input("> ")
            try:
                index = int(user_input)
                if index == 1:
                    print("Mystery Man: 'Who knows?")
                elif index == 2:
                    having = []
                    missing = []
                    if game.hero.key_item_check(item_sheet.robot_chip):
                        having.append("ROBOT CHIP")
                    else:
                        missing.append("ROBOT CHIP")
                    if game.hero.key_item_check(item_sheet.crab_shell):
                        having.append("CRAB SHELL")
                    else:
                        missing.append("CRAB SHELL")
                    if game.hero.key_item_check(item_sheet.gorilla_paw):
                        having.append("GORILLA PAW")
                    else:
                        missing.append("GORILLA PAW")
                    if not missing:
                        if self.asked_leave:
                            print(f"Very good, {game.hero.name}! You brought me the items I desired!")
                            print("I shall now show you the secret passageway!")
                        else:
                            print("If you want to leave bring me a ROBOT CHIP, a CRAB SHELL and a GORILLA PAW.")
                            print("What? You already have those? How did you...whatever. Just give them to me.")
                            print(f"Very well, {game.hero.name}! I shall now show you the secret passageway!")
                            if rooms["gambler_stand"].objects[0].gambler_dead:
                                print("By the way, I heard you killed the gambler. Never liked the dude, to be honest.")

                    elif having:
                        print(f"You still need to bring me {', '.join(missing)}.")
                        print(f"Remember, you already have {', '.join(having)}.")
                    else:
                      print(f"You can try to leave. Bring me a ROBOT CHIP, a CRAB SHELL, and a GORILLA PAW\n")
                    self.asked_leave = True




                elif index == 3:
                    print(f"Big mistake.")
                    self.fight(game, room)
                    return
                elif index == 4:
                    return
            except ValueError:
                print(f"Input '{user_input}' not a valid choice!")





    def fight(self, game: Game, room: Room):
        result = start_battle(game.hero, enemy_sheet.mystery_man)
        if result == Outcome.WIN:
            print("The Mystery Man died...or did he?")
            room.objects.remove(self)
        elif result == Outcome.LOSS:
            print("You died. Game Over!")
            exit()

class DoorGamblerStand(RoomObject):
    GOTO = "Go to the GAMBLER STAND"

    def __init__(self):
        self.interactions = [
            DoorGamblerStand.GOTO,
        ]

    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == DoorGamblerStand.GOTO:
            print("You're walking towards the gambler stand.")
            game.select_room("gambler_stand")

class DoorHotel(RoomObject):
    GOTO = "Go to the HOTEL"

    def __init__(self):
        self.interactions = [
            DoorHotel.GOTO,
        ]

    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == DoorHotel.GOTO:
            print("You're walking towards the hotel.")
            game.select_room("hotel")


class DoorBeach(RoomObject):
    GOTO = "Go to the BEACH"

    def __init__(self):
        self.interactions = [
            DoorBeach.GOTO,
        ]

    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == DoorBeach.GOTO:
            print("You're walking towards the beach.")
            game.select_room("beach")

class IslandDocks(Room):
    def __init__(self):
        self.objects = [
            MysteryMan(),
            DoorGamblerStand(),
            DoorHotel(),
            DoorBeach()
        ]

    def describe(self, game: Game):
        print("You are at the island docks")
