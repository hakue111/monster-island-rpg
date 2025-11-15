import abc
import typing

if typing.TYPE_CHECKING:
    from rpg.room.roomobject import RoomObject
    from rpg.game import Game


class Room(abc.ABC):
    objects: list['RoomObject']

    @abc.abstractmethod
    def describe(self, game: 'Game'): ...
