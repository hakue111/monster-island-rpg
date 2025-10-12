import abc

from rpg.game import Game
from rpg.room.roomobject import RoomObject


class Room(abc.ABC):
    objects: list[RoomObject]

    @abc.abstractmethod
    def describe(self, game: Game): ...
