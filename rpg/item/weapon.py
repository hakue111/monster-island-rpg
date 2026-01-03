class Weapon:
    def __init__(self,
                 name: str,
                 dmg: int,
                 value: int):
        self.name = name
        self.dmg = dmg
        self.value = value

    def __str__(self):
        return f"Weapon(name='{self.name}', dmg={self.dmg}, value={self.value})"

