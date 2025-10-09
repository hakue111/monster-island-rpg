from island_docks import IslandDocks

def start_game():
    answer = input("Would you like to experience what Monster Island has in store for you? (yes/no)\n > ")
    if answer.casefold().strip() == "no".casefold():
        print("That's too bad...Oh well, maybe next time?")
    elif answer.casefold().strip() == "yes".casefold():
        print("Welcome to 'MONSTER ISLAND'!")
        input("Press Enter to continue...")
        IslandDocks("Island Docks", "Docks of the island, lol.").boarding()
    elif answer != "yes" or answer != "no":
        print("Invalid input.")
        start_game()

if __name__ == '__main__':
    start_game()
