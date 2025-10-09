from effect import HealEffect
from item import *

potion:ConsumableItem = ConsumableItem("Potion", "Restores 40 HP.", 1)
potion.add_effect(HealEffect(40))