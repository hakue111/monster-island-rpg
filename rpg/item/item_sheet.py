from rpg.item.effect import HealEffect
from rpg.item.item import ConsumableItem, KeyItem

potion: ConsumableItem = ConsumableItem("Potion", "Restores 40 HP.", 1)
potion.add_effect(HealEffect(40))

robot_chip: KeyItem = KeyItem("Robot Chip", "A mysterious computer chip that once belonged to the Robot Bellboy", 1)
crab_shell: KeyItem = KeyItem("Crab Shell", "A mysterious crab shell that once belonged to the Huge Crab", 1)
gorilla_fist: KeyItem  = KeyItem("Gorilla Fist", "A mysterious gorilla fist that belonged to said animal once", 1)

