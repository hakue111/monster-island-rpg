from rpg.item.effect import RestoreHPEffect, RestoreMPEffect
from rpg.item.item import ConsumableItem, KeyItem

# CONSUMABLE ITEMS
potion: ConsumableItem = ConsumableItem("Potion", "Restores 40 HP.", 1)
potion.add_effect(RestoreHPEffect(40))

hi_potion: ConsumableItem = ConsumableItem("Hi-Potion", "Restores 60 HP.", 1)
hi_potion.add_effect(RestoreHPEffect(60))

mega_potion: ConsumableItem = ConsumableItem("Mega-Potion", "Restores 100 HP.", 1)
mega_potion.add_effect(RestoreHPEffect(100))

ether: ConsumableItem = ConsumableItem("Ether", "Restores 40 MP.", 1)
ether.add_effect(RestoreMPEffect(40))

hi_ether: ConsumableItem = ConsumableItem("Hi-Ether", "Restores 60 MP.", 1)
hi_ether.add_effect(RestoreMPEffect(60))

mega_ether: ConsumableItem = ConsumableItem("Mega-Ether", "Restores 100 MP.", 1)
ether.add_effect(RestoreMPEffect(100))

elixir: ConsumableItem = ConsumableItem("Elixir", "Restores 100 HP and 100 MP", 1)
elixir.add_effect(RestoreHPEffect(100))
elixir.add_effect(RestoreMPEffect(100))

#KEY ITEMS
robot_chip: KeyItem = KeyItem("Robot Chip", "A mysterious computer chip that once belonged to the Robot Bellboy", 1)
crab_shell: KeyItem = KeyItem("Crab Shell", "A mysterious crab shell that once belonged to the Huge Crab", 1)
gorilla_paw: KeyItem  = KeyItem("Gorilla Paw", "A mysterious gorilla fist that belonged to said animal once", 1)

