class Room:
    def __init__(self,
                 name: str,
                 description: str
                 ):
        self.name = name
        self.description = description
        self.north: Room = None
        self.east: Room = None
        self.south: Room = None
        self.west: Room = None

        def enter_room(self):
            raise NotImplementedError

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
