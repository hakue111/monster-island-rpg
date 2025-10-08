import random
import character
import item_sheet
from battle_scene import *
from character import *
from weapon import *
from room_state import Room

class GamblerRoom(Room):
    def __init__(self, name: str,
                 description: str
                 ):
        super().__init__(name, description)
        self.gambler: Enemy = Enemy("Gambler", 50, fists)
        self.annoyance: int = 0



    def shell_game(self):
        print("The Gambler shuffles the shells.")
        shells = [1,2,3]
        shuffled = random.choice(shells)
        while True:
            if self.annoyance >= 3:
                return None
            choice = input("Please select one of three shells (1/2/3).\n> ")
            if choice == str(shuffled):
                print("You Win!")
                print(f"The correct shell was shell no. {shuffled}")
                return True
            elif choice not in [str(shell) for shell in shells]:
                print("Stop fucking around! Give me an answer! 1, 2 or 3!")
                self.annoyance += 1
            elif choice != shuffled:
                print("You lose!")
                print(f"The correct shell was shell no. {shuffled}")
                return False

    def gambler_stand(self):
        print("You enter the shell game stand.")
        print(f"Gambler: Hello, would you like to play a game?\nIt's simple: I will hide this little ball under one of three shells.\nI will then shuffle the shells. You have one guess.")
        print(f"But don't try to piss me off!")
        accepted = False
        while not accepted:
            choice = input("Do you accept the challenge?(yes/no)\n> ")
            if choice.casefold().strip() == "yes".casefold():
                accepted = True
            else:
                print(f"Gambler: Come on, it's free...")
                self.annoyance += 1
            if self.annoyance >= 3:
                print(f"If you don't want to play, I will have to kill you!!")
                gambler_fight()
        if self.annoyance <3:
            print(f"Very well. Let's begin!")
            has_won = shell_game()
            if has_won is None:
                print("Shut the FUCK UP!! I'M GONNA KILL YOU!")
                gambler_fight()
            elif has_won is True:
                print("Lucky shot...")
                character.player.add_consumable(item_sheet.potion, 1)
            elif has_won is False:
                print("You lost, which means I'm going to take one of YOUR items!")
                character.player.add_consumable(item_sheet.potion, -1)


    def gambler_fight(self):
        result = start_battle(character.player, self.gambler)
        if result == "win":
            print("The gambler dies.")
        elif result == "lose":
            print("You died (lol). Game Over!")


