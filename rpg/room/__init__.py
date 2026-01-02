from rpg.room.beach import Beach
from rpg.room.gambler_stand import GamblerStand
from rpg.room.hotel import Hotel
from rpg.room.island_docks import IslandDocks

rooms = {
    "island_docks": IslandDocks(),
    "gambler_stand": GamblerStand(),
    "hotel": Hotel(),
    "beach": Beach(),
}