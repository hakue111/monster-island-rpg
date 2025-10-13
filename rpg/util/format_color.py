import enum
from typing import Optional

CODE_REST = "\033[0m"

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

CODE_BOLD = "\033[1m"
CODE_UNDERLINE = "\033[4m"

def format_text(
        color: Optional[Color],
        text: str,
        bold: bool = False,
        underline: bool = False,
) -> str:
    result = ""
    if color is not None:
        result += color.value
    if bold:
        result += CODE_BOLD
    if underline:
        result += CODE_UNDERLINE
    result += text
    result += CODE_REST
    return result