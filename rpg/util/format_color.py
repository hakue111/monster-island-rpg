import enum
from typing import Optional

RESET = "\033[0m"

class Color(enum.Enum):
    BLUE = "\033[94m"
    GREY = "\033[90m"
    YELLOW = "\033[93m"
    BLACK = "\033[90m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    WHITE= "\033[97m"
    RED = "\033[91m"

def format_text(color: Optional[Color], text: str) -> str:
    if color is None:
        return text
    return f"{color.value}{text}{RESET}"