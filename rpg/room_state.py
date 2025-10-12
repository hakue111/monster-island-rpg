from typing import Optional

from rpg.scene import Scene


class Room:
    name: str
    description: str
    north: Optional['Room']
    east: Optional['Room']
    south: Optional['Room']
    west: Optional['Room']
    scenes: list[Scene]

    def __init__(self,
                 name: str,
                 description: str
                 ):
        self.name = name
        self.description = description
        self.north = None
        self.east = None
        self.south = None
        self.west = None
        self.scenes = []

    def add_scene(self, scene: Scene):
        self.scenes.append(scene)

    def enter_room(self):
        print(f"Enter location '{self.name}'")
        print(f"What do you want to do?")
        for scene in self.scenes:
            print(f"{scene.key}: {scene.name}")
        print("Exit: Change room")
        self.user_choice()

    def user_choice(self):
        user_input = input("> ")
        if user_input == "exit":
            self.goto_room()
            return None
        for scene in self.scenes:
            if scene.key.casefold().strip() == user_input.casefold().strip():
                scene.play_scene()
                return None
        print(f"No choice for '{user_input}' found.")
        self.enter_room()
        return None

    def goto_room(self):
        print(f"Choose where you want to go next:\n"
              f"North:{self.north.name}\n"
              f"East:{self.east.name}\n"
              f"South:{self.south.name}\n"
              f"West:{self.west.name}")
        user_input = input("North | East | South | West\n> ")
        if user_input.casefold().strip() == "north":
            self.north.enter_room()
        if user_input.casefold().strip() == "east":
            self.east.enter_room()
        if user_input.casefold().strip() == "south":
            self.south.enter_room()
        if user_input.casefold().strip() == "west":
            self.south.enter_room()
