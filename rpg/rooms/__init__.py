from rpg.rooms.gambler_stand import gambler_stand
from rpg.rooms.island_docks import island_docks

gambler_stand.south = island_docks
island_docks.north = gambler_stand
