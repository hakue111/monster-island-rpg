from rpg.character.character import Hero
from rpg.cutscene.boarding import BoardingScene
from rpg.game import Game
from rpg.room import rooms


class Rpg(Game):
    def __init__(self, initial_room: str):
        self.current_room = initial_room
        self.hero = Hero(name="Jane Doe", hp=100, mp=50, elemental="neutral")

    def loop(self):
        BoardingScene().run(self)
        while True:
            self.interact()

    def select_room(self, room: str):
        selected_room = rooms.get(room)
        selected_room.describe(self)
        self.current_room = room

    def interact(self):
        room = rooms.get(self.current_room)
        interactions = []
        for obj in room.objects:
            for interaction in obj.interactions:
                interactions.append((obj, interaction))
        for index in range(len(interactions)):
            obj, interaction = interactions[index]
            print(f"{index + 1}. {interaction}")
        while True:
            try:
                choice = int(input("> "))
                obj, interaction = interactions[choice - 1]
                obj.interact(self, room, interaction)
                break
            except Exception:
                print("Invalid choice.")
