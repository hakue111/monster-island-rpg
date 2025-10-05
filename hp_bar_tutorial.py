# HP bar should have the following properties:
# length
# maximum value
# current value
# symbol for both remaining and lost amount
# decorating barriers, if it's colored and its color

# it will have two methods:
# an update method to update its current value
# a draw method to print it to the screen

import os

os.system("")

class HpBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"default": "\033[0m",
                    "blue": "\033[94m",
                    "grey": "\033[90m",
                    "yellow": "\033[93m",
                    "black": "\033[90m",
                    "cyan": "\033[96m",
                    "green": "\033[92m",
                    "magenta": "\033[95m",
                    "white": "\033[97m",
                    "red": "\033[91m"
                    }
    def __init__(self,
                 entity,
                 length: int = 20,
                 is_colored: bool = True,
                 color: str = "") -> None:
        self.entity = entity
        self.length = length

        self.max_value = entity.hp_max
        self.current_value = entity.hp

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]


    def update(self) -> None:
        self.current_value = self.entity.hp


    def draw(self) -> None:
        remaining_bars = round(self.current_value/ self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s HP: {self.entity.hp}/{self.entity.hp_max}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored == True else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored == True else ''}"
              f"{self.barrier}")

