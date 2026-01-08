from rpg.item.effect import RestoreHPEffect, RestoreMPEffect
from rpg.item.item import ConsumableItem, KeyItem

# CONSUMABLE ITEMS
##TIER 1
potion: ConsumableItem = ConsumableItem("Potion", "Restores 40 HP.")
potion.add_effect(RestoreHPEffect(40))

ether: ConsumableItem = ConsumableItem("Ether", "Restores 40 MP.")
ether.add_effect(RestoreMPEffect(40))

##TIER 2
hi_potion: ConsumableItem = ConsumableItem("Hi-Potion", "Restores 60 HP.")
hi_potion.add_effect(RestoreHPEffect(60))

hi_ether: ConsumableItem = ConsumableItem("Hi-Ether", "Restores 60 MP.")
hi_ether.add_effect(RestoreMPEffect(60))

##TIER 3
mega_potion: ConsumableItem = ConsumableItem("Mega-Potion", "Restores 100 HP.")
mega_potion.add_effect(RestoreHPEffect(100))

mega_ether: ConsumableItem = ConsumableItem("Mega-Ether", "Restores 100 MP.")
mega_ether.add_effect(RestoreMPEffect(100))

elixir: ConsumableItem = ConsumableItem("Elixir", "Restores 100 HP and 100 MP")
elixir.add_effect(RestoreHPEffect(100))
elixir.add_effect(RestoreMPEffect(100))

#KEY ITEMS
robot_chip: KeyItem = KeyItem("Robot Chip", "A mysterious computer chip that once belonged to the Robot Bellboy", 1)
crab_shell: KeyItem = KeyItem("Crab Shell", "A mysterious crab shell that once belonged to the Huge Crab", 1)
gorilla_paw: KeyItem  = KeyItem("Gorilla Paw", "A mysterious gorilla fist that belonged to said animal once", 1)

