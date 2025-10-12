from rpg.item.effect import HealEffect
from rpg.item.item import ConsumableItem

potion: ConsumableItem = ConsumableItem("Potion", "Restores 40 HP.", 1)
potion.add_effect(HealEffect(40))
