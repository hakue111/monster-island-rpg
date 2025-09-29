# Player stat sheet

class Player:
    def __init__(self, name, hp, atk, dfn, armor, tf_stage, is_cursed, is_defeated, is_caught):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dfn = dfn
        self.armor = armor
        self.tf_stage = 0
        self.is_cursed = False
        is_defeated = False
        is_caught = False


    def take_dmg(self, dmg):
        self.health -= dmg


# Apply curse to player
    def apply_curse(self):
        self.is_cursed = True
        self.curse_level = 1
        print(f"You feel weird...")



class Enemy:
    def __init__(self, name, hp, atk, dfn, armor, is_defeated):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dfn = dfn
        self.armor = armor
        is_defeated = False



enemy1 = Enemy("Regular Monster", 50, 10, 10, 10, False)
enemy2 = Enemy("Squad Leader Monster", 75, 20, 20, 15, False)
enemy3 = Enemy("Elite Monster", 100, 30, 30, 30, False)
enemy4 = Enemy("Spy", 30, 5, 10, 0, False)
enemy5 = Enemy("Boss", 150, 50, 40, 45, False)
















