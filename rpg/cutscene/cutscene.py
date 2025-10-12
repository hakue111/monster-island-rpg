import abc

from rpg.game import Game


class Cutscene(abc.ABC):
    @abc.abstractmethod
    def run(self, game: Game): ...