from rpg.character import enemy_sheet
from rpg.character.battle_scene import start_battle
from rpg.character.outcome import Outcome
from rpg.game import Game
from rpg.room.room import Room
from rpg.room.roomobject import RoomObject

class MysteryMan(RoomObject):
    TALK = "Talk to the MYSTERY MAN"
    LOOK = "Look at the MYSTERY MAN"
    CHALLENGE = "Challenge the MYSTERY MAN to a duel"

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
                    print(f"Mystery Man: 'What do you think MONSTER ISLAND means, dumbass?")
                elif index == 2:
                    print(f"You can try to leave if you want...")
                elif index == 3:
                    print(f"I'm going to teach you some manners, you little bastard!")
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
            print("You died (lol). Game Over!")
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
