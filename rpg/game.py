import abc

from rpg.character.character import Hero


class Game(abc.ABC):
    current_room: str
    hero: Hero

    def select_room(self, room: str):
        self.current_room = room
