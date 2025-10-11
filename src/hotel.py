from src.character import Enemy
from src.room_state import Room
from src.weapon import *


class HotelRoom(Room):
    def __init__(self, name: str,
                 description:str
                 ):
        super().__init__(name, description)
        self.robot_bellboy: Enemy = Enemy("Robot Bellboy", 1000, iron_sword)

