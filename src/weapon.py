class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 dmg: int,
                 value: int):

        self.name = name
        self.weapon_type = weapon_type
        self.dmg = dmg
        self.value = value

iron_sword = Weapon(name = "Iron Sword",
                    weapon_type = "sharp",
                    dmg = 5,
                    value = 10)

short_bow = Weapon(name = "Short Bow",
                   weapon_type = "ranged",
                   dmg = 4,
                   value = 8)

fists = Weapon(name = "Fists",
               weapon_type = "blunt",
               dmg = 2,
               value = 0)

robot_claw = Weapon(name = "Robot Claw",
                    weapon_type = "mechanical",
                    dmg = 10,
                    value = 50)
