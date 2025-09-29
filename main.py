import random
from settings import *
from os.path import join
from entities import Player


def start_game():
    answer = input("Would you like to experience what Monster Island has in store for you? (yes/no)\n > ")
    if answer.lower().strip() == "no":
        print("That's too bad...Oh well, maybe next time?")
    elif answer.lower().strip() == "yes":
        print("Welcome to 'MONSTER ISLAND'!")
        input("Press Enter to continue...")
        boarding()
    elif answer != "yes" or answer != "no":
        print("Invalid input. Please answer (yes/no) and press Enter.\n> ")

def boarding():
    print("You have won a free vacation on Monster Island.")
    print("The name already indicates that this island means danger.")
    input("Press Enter to continue...")
    print("You are standing on the docks. With your baggage and your ticket in your hands, you are about to board the ferry.")
    print("A mysterious man checks your ticket.")
    input("Press Enter to continue...")
    print("Mysterious Man: What is your name?")
    name_choice = input("@Player: Please enter your name and press Enter:\n> ")
    print(f"Mysterious Man: So, you are {name_choice}? Very well. Please board the ferry. We are departing soon.")
    print(f'{name_choice} boards the ferry.')
    print(f"The ferry horn honks and the ship departs. Soon, the mainland will be out of sight.")
    print(f"{name_choice}, you are going on a dark and mysterious adventure. Be careful...")
    input("Press Enter to continue...")
    print("You arrive on Monster Island. You are greeted by the mysterious man")
    print(f"Mysterious man: Welcome to Monster Island, {name_choice}. Enjoy your stay...")
    print("There are three places you can go now: The hotel, the mansion and the forest. Where do you go?")
    choice = input("Please enter where you want to go (hotel/mansion/forest)\n>")
    if choice.lower().strip() == "hotel":
        print(f"{name_choice} goes to the hotel.")
        hotel()
    elif choice.lower().strip() == "mansion":
        print(f"{name_choice} goes to the mansion.")
        mansion()
    elif choice.lower().strip() == "forest":
        print(f"{name_choice} goes to the forest")
        forest()
    else:
        print("Invalid input. Please input hotel/mansion/forest and press Enter")


start_game()


hotel()
print("You enter the hotel. A bellboy is greeting you and takes your luggage.")
print("The bellboy takes you to your hotel room.")
input("Press Enter to continue...")
print(f"Bellboy: 'This is your room, {name_choice}. Have fun...\n The bellboy leaves.")
choice = input("Do you want to stay and rest for a while? (yes/no)\n> ")
if choice == "yes":
    print("You decide to get some rest in your hotel room.")
    print("You get some hours of sleep...")
    input("Press Enter to continue...")
    hotel_wake()


mansion()
pass

forest()
pass






