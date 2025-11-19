import random
from time import sleep
from typing import Optional

from rpg.character import enemy_sheet
from rpg.character.battle_scene import start_battle
from rpg.character.outcome import Outcome
from rpg.game import Game
from rpg.item import item_sheet
from rpg.item.item import Item, KeyItem, ConsumableItem
from rpg.room.room import Room
from rpg.room.roomobject import RoomObject


class Gambler(RoomObject):
    LOOK = "Look at the GAMBLER"
    TALK = "Play the GAMBLER's game of chance"
    FIGHT = "Attack the shady GAMBLER"
    jackpot: list[ConsumableItem | KeyItem] = [
        item_sheet.potion,
        item_sheet.hi_potion,
        item_sheet.mega_potion,
        item_sheet.ether,
        item_sheet.hi_ether,
        item_sheet.mega_ether,
        item_sheet.elixir,
        item_sheet.robot_chip,
        item_sheet.crab_shell,
        item_sheet.gorilla_paw
        ]

    annoyance: int
    game_counter: int
    already_explained: bool

    def __init__(self):
        self.interactions = [
            Gambler.LOOK,
            Gambler.TALK,
            Gambler.FIGHT,
        ]
        self.annoyance = 0
        self.game_counter = 0
        self.already_explained = False

    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == Gambler.LOOK:
            print("The gambler tries to convince you to try his game")
        if interaction == Gambler.TALK:
            self.talk(game, room)
        elif interaction == Gambler.FIGHT:
            self.fight(game, room)

    def talk(self, game: Game, room: Room):
        if self.game_counter > 5:
            print(f"Gambler: 'Sorry, but I don't want to play anymore.")
            return
        if not self.already_explained:
            self.already_explained = True
            print("Gambler: 'Would you like to play a game?'")
            print("It's simple: I will hide this little ball under one of three shells.")
            print("I will then shuffle the shells. You must pick the one with the ball under it.")
            print("You have one guess.")
            print("Do you accept the challenge?(yes/no)")
            accepted = False
            while not accepted:
                choice = input("> ")
                if choice.casefold().strip() == "yes".casefold():
                    accepted = True
                else:
                    print(f"...")
                    self.annoyance += 1
                if self.annoyance == 1:
                    print(f"Come one, please decide and stop wasting my time.")
                elif self.annoyance == 2:
                    print("Please decide, you're starting to piss me off!")
                elif self.annoyance >= 3:
                    print(f"STOP. PISSING. ME. OFF!")
                    self.fight(game, room)
                    return
        if self.annoyance < 3:
            print(f"Very well. Let's begin!")
            outcome = self.shell_game()
            if outcome is None:
                print("Shut the fuck up and let's fight instead!")
                self.fight(game, room)
            elif outcome == Outcome.WIN:
                sleep(1)
                print("It's your lucky day!")
                random_item = random.choice(self.jackpot)
                self.jackpot.remove(random_item)
                if isinstance(random_item, ConsumableItem):
                    print("You win a consumable item.")
                    game.hero.add_consumable(random_item, 1, True)
                else:
                    print("You win a very special item!")
                    game.hero.add_key_item(random_item, 1, True)
                self.game_counter += 1
            elif outcome == Outcome.LOSS:
                print("You lost, which means I'm going to take one of YOUR items!")
                random_item = random.randrange(0,len(game.hero.consumables) - 1)
                game.hero.add_consumable(game.hero.consumables[random_item], -1, True)
                self.game_counter += 1


    def shell_game(self) -> Optional[Outcome]:
        print("The Gambler shuffles the shells.")
        shells = [1, 2, 3]
        shuffled = random.choice(shells)
        while True:
            if self.annoyance >= 3:
                return None
            print("Please select one of three shells (1/2/3).")
            choice = input("> ")
            if choice == str(shuffled):
                print("You Win!")
                print(f"The correct shell was shell no. {shuffled}")
                return Outcome.WIN
            elif choice not in [str(shell) for shell in shells]:
                print("Stop fucking around! Give me an answer! 1, 2 or 3!")
                self.annoyance += 1
            elif choice != shuffled:
                print("You lose!")
                print(f"The correct shell was shell no. {shuffled}")
                return Outcome.LOSS

    def fight(self, game: Game, room: Room):
        result = start_battle(game.hero, enemy_sheet.gambler, True)
        if result == Outcome.WIN:
            print("The gambler dies.")
            game.choices["gambler_dead"] = True
            room.objects.remove(self)
            room.objects.append(GamblingStandCounter())
        elif result == Outcome.LOSS:
            print("You died. Game Over!")
            exit()

class GamblingStandCounter(RoomObject):
    LOOK = "Look behind the COUNTER"

    used: bool

    def __init__(self):
        self.used = False
        self.interactions = [
            GamblingStandCounter.LOOK,
        ]

    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == GamblingStandCounter.LOOK:
            if self.used:
                print("There's nothing here")
            else:
                print("Behind the counter, you find a large chest.")
                user_input = input("Open it? (yes/no)\n> ")
                if user_input.casefold().strip() == "yes":
                    print("You open the chest and find an Elixir and a Hi-Ether!")
                    game.hero.add_consumable(item_sheet.elixir, 1, True)
                    game.hero.add_consumable(item_sheet.hi_ether, 1, True)
                    self.used = True
                else:
                    print("You decide to not open the chest.")



class DoorIslandDocks(RoomObject):
    GOTO = "Return to the ISLAND DOCKS"

    def __init__(self):
        self.interactions = [
            DoorIslandDocks.GOTO
        ]

    def interact(self, game: Game, room: Room, interaction: str):
        if interaction == DoorIslandDocks.GOTO:
            print("You're walking back towards the docks.")
            game.select_room("island_docks")

class GamblerStand(Room):
    def __init__(self):
        self.objects = [
            Gambler(),
            DoorIslandDocks(),
        ]

    def describe(self, game: Game):
        has_gambler = False
        for obj in self.objects:
            if isinstance(obj, Gambler):
                has_gambler = True

        if has_gambler:
            print("You are at a shady old carnival stand, with an even shadier GAMBLER standing at the counter.")
            print("The gambler tries to convince you to try his game")
        else:
            print("It's the old gambler's stand, but now it's empty and starting to fall apart")
