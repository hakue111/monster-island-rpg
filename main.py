import random
import item_sheet
from gambler_stand import gambler_stand
from settings import *
from os.path import join
from character import *
import character

def start_game():
    answer = input("Would you like to experience what Monster Island has in store for you? (yes/no)\n > ")
    if answer.casefold().strip() == "no".casefold():
        print("That's too bad...Oh well, maybe next time?")
    elif answer.casefold().strip() == "yes".casefold():
        print("Welcome to 'MONSTER ISLAND'!")
        input("Press Enter to continue...")
        boarding()
    elif answer != "yes" or answer != "no":
        print("Invalid input.")
        start_game()

def boarding():
    print("You have won a free vacation on Monster Island.")
    print("The name already indicates that this island means danger.")
    input("Press Enter to continue...")
    print("You are standing on the docks. With your baggage and your ticket in your hands, you are about to board the ferry.")
    print("A mysterious man checks your ticket.")
    input("Press Enter to continue...")
    print("Mysterious Man: What is your name?")
    name_choice = input("@Player: Please enter your name and press Enter:\n> ")
    character.player = Hero(name_choice, 100)
    print(f"Mysterious Man: So, you are {name_choice}? Please board the ferry. We are departing soon.")
    print(f"Mysterious Man: By the way, I have something useful for you.")
    # give player a potion
    character.player.add_consumable(item_sheet.potion, 5)
    print(f'{name_choice} boards the ferry.')
    print(f"The ferry horn honks and the ship departs. Soon, the mainland will be out of sight.")
    print(f"{name_choice}, you are going on a dark and mysterious adventure. Be careful...")
    input("Press Enter to continue...")

    print("You arrive on Monster Island. You are greeted by the mysterious man")
    print(f"Mysterious man: Welcome to Monster Island, {name_choice}. Enjoy your stay...")
    print("There are three places you can go now: The Hotel, the gambler stand and the forest. Where do you go?")
    while True:
        choice = input("Please enter where you want to go (Hotel/Gambler Stand/forest)\n>")
        if choice.casefold().strip() == "Hotel".casefold():
            print(f"{name_choice} goes to the Hotel.")
            hotel()
        elif choice.casefold().strip() == "Gambler Stand".casefold():
            print(f"{name_choice} goes to the Gambler Stand.")
            gambler_stand()
        elif choice.casefold().strip() == "Forest".casefold():
            print(f"{name_choice} goes to the Forest")
            forest()
        else:
            print("Invalid input. Please input Hotel/Gambler Stand/Forest and press Enter")






start_game()


#hotel()
#print("You enter the hotel. A bellboy is greeting you and takes your luggage.")
#print("The bellboy takes you to your hotel room.")
#input("Press Enter to continue...")
#print(f"Bellboy: 'This is your room, {name_choice}. Have fun...\n The bellboy leaves.")
#choice = input("Do you want to stay and rest for a while? (yes/no)\n> ")
#if choice == "yes":
 #   print("You decide to get some rest in your hotel room.")
  #  print("You get some hours of sleep...")
   # input("Press Enter to continue...")
    #hotel_wake()


#mansion()
pass

#forest()
pass


















