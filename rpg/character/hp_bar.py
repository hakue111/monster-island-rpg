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

class HpMpBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "▒"
    barrier: str = "|"

    def __init__(self,
                 entity,
                 length: int = 20,
                 hp_color: Optional[Color] = None,
                 mp_color: Optional[Color] = None) -> None:
        self.entity = entity
        self.length = length

# hit points (HP)
        self.max_hp_value = entity.hp_max
        self.current_hp_value = entity.hp
        self.hp_color = hp_color
# mana points (MP)
        self.max_mp_value = entity.mp_max
        self.current_mp_value = entity.mp
        self.mp_color = mp_color

    def update(self) -> None:
        self.current_hp_value = self.entity.hp
        self.current_mp_value = self.entity.mp

    def draw(self) -> None:
    # draw HP bar
        remaining_bars_hp = round(self.current_hp_value / self.max_hp_value * self.length)
        lost_bars_hp = self.length - remaining_bars_hp

        remaining_bars_mp = round(self.current_mp_value / self.max_mp_value * self.length)
        lost_bars_mp = self.length - remaining_bars_mp
    # f string for HP and MP gauges
        print(format_text(color=None, bold=True, text=self.entity.name))
        hp_text = f"HP: {self.entity.hp}/{self.entity.hp_max}".ljust(self.length)
        mp_text= f"MP: {self.entity.mp}/{self.entity.mp_max}".ljust(self.length)
        print(hp_text, mp_text)
        print(
            format_text(
                self.hp_color,
                f"{remaining_bars_hp * self.symbol_remaining}{lost_bars_hp * self.symbol_lost}"
            ),
    # draw MP bar
            format_text(
                self.mp_color,
                f"{remaining_bars_mp * self.symbol_remaining}{lost_bars_mp * self.symbol_lost}"
            ),
        )