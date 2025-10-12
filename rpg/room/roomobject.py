import abc
import typing

from rpg.game import Game

if typing.TYPE_CHECKING:
    from rpg.room.room import Room


class RoomObject(abc.ABC):
    interactions: list[str]

    @abc.abstractmethod
    def interact(self, game: Game, room: 'Room', interaction: str): ...
