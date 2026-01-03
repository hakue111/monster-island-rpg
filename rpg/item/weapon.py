class Weapon:
    def __init__(self,
                 name: str,
                 dmg: int,
                 value: int,
                 tier: int):
        self.name = name
        self.dmg = dmg
        self.value = value
        self.tier = tier

    def __str__(self):
        return f"Weapon(name='{self.name}', dmg={self.dmg}, value={self.value}, tier={self.tier})"

