import random

import character
from battle_scene import *
from character import *
from weapon import *

gambler: Enemy = Enemy("Gambler", 50, fists)


annoyance = 0

def shell_game():
    global annoyance #this variable is not a local variable of this function
    print("The Gambler shuffles the shells.")
    shells = [1,2,3]
    shuffled = random.choice(shells)
    while True:
        if annoyance >= 3:
            return None
        choice = input("Please select one of three shells (1/2/3).\n> ")
        if choice == str(shuffled):
            print("You Win!")
            print(f"The correct shell was shell no. {shuffled}")
            return True
        elif choice not in [str(shell) for shell in shells]:
            print("Stop fucking around! Give me an answer! 1, 2 or 3!")
            annoyance += 1
        elif choice != shuffled:
            print("You lose!")
            print(f"The correct shell was shell no. {shuffled}")
            return False

def gambler_stand():
    global annoyance
    print("You enter the shell game stand.")
    print(f"Gambler: Hello, would you like to play a game?\nIt's simple: I will hide this little ball under one of three shells.\nI will then shuffle the shells. You have one guess.")
    accepted = False
    while not accepted:
        choice = input("Do you accept the challenge?(yes/no)\n> ")
        if choice.casefold().strip() == "yes".casefold():
            accepted = True
        else:
            print(f"Gambler: Come on, it's free...")
            annoyance += 1
    print(f"Very well. Let's begin!")
    has_won = shell_game()
    if has_won is None:
        gambler_fight()
    elif has_won is True:
        print("Lucky shot...")
        # receive item
    elif has_won is False:
        print("Well, well, well. The game might have been free, but that doesn't mean there won't be any consequences!")
        # lose item


def gambler_fight():
    print("SHUT THE FUCK UP I'M GONNA KILL YOU!")
    result = start_battle(character.player, gambler)
    if result == "win":
        print("The gambler dies. Lol.")
    elif result == "lose":
        print("You died (lol). Game Over!")


