from typing import TypeVar

T = TypeVar('T')

def choose(options: list[T]) -> T:
    while True:
        try:
            choice = int(input("> "))
            return options[choice - 1]
        except Exception:
            print("Invalid choice.")
