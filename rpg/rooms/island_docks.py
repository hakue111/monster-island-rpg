from rpg import character, enemy_sheet
from rpg.battle_scene import start_battle
from rpg.room_state import Room
from rpg.scene import SceneOptionLambda


def talk_mysteryman(self):
    print("You are talking to the Mystery Man.")
    input("Press Enter to continue...")
    print(f"So, {character.player.name}, what do you want to know?")
    while True:
        user_input = input(
            "1: 'What is this place?'\n2: 'How can I leave?'\n3: 'Why did you pick that awkward name, Mystery Man? Are you stupid?'\n> ")
        try:
            index = int(user_input)
            if index == 1:
                print(f"Mystery Man: 'What do you think MONSTER ISLAND means, dumbass?")
            elif index == 2:
                print(f"You can try to leave if you want...")
            elif index == 3:
                print(f"I'm going to teach you some manners, you little bastard!")
                self.fight_mysteryman()
        except ValueError:
            print(f"Input '{user_input}' not a valid choice!")


def fight_mysteryman(self):
    result = start_battle(character.player, enemy_sheet.mystery_man)
    if result == "win":
        print("The Mystery Man died...or did he?")
        # how does game return to room selection after this?
    elif result == "lose":
        print("You died (lol). Game Over!")
        exit


island_docks: Room = Room("Island Docks", "This is where the Monster Island Ferry stops. Your journey begins here.")
island_docks.add_scene(SceneOptionLambda(talk_mysteryman))
