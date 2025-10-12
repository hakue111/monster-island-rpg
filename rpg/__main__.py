from rpg.rooms.island_docks import island_docks


def start_game():
    answer = input("Would you like to experience what Monster Island has in store for you? (yes/no)\n > ")
    if answer.casefold().strip() == "no".casefold():
        print("That's too bad...Oh well, maybe next time?")
    elif answer.casefold().strip() == "yes".casefold():
        print("Welcome to 'MONSTER ISLAND'!")
        input("Press Enter to continue...")
        # IslandDocks("Island Docks", "You begin your journey here.").boarding()
        island_docks.enter_room()
    elif answer != "yes" or answer != "no":
        print("Invalid input.")
        start_game()


if __name__ == '__main__':
    start_game()
