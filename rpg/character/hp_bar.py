# HP bar should have the following properties:
# length
# maximum value
# current value
# symbol for both remaining and lost amount
# decorating barriers, if it's colored and its color
from typing import Optional

from rpg.util.format_color import Color, format_text


# it will have two methods:
# an update method to update its current value
# a draw method to print it to the screen

class HpBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "▒"
    barrier: str = "|"

    def __init__(self,
                 entity,
                 length: int = 20,
                 color: Optional[Color] = None) -> None:
        self.entity = entity
        self.length = length

        self.max_value = entity.hp_max
        self.current_value = entity.hp
        self.color = color

    def update(self) -> None:
        self.current_value = self.entity.hp

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s HP: {self.entity.hp}/{self.entity.hp_max}")
        print(
            f"{self.barrier}",
            format_text(
                self.color,
                f"{remaining_bars * self.symbol_remaining}{lost_bars * self.symbol_lost}"
            ),
            f"{self.barrier}",
        )
