class Entity:
    def __init__(self, name, hp, atk, dfn, armor, is_dead, is_cursed):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dfn = dfn
        self.armor = armor
        self.is_cursed = is_cursed


    def attack(self, target): -> None
        target.hp -= self.dmg
        target.hp -= max(target.hp, 0)



    def is_dead(self):
        return self.hp <= 0

    def take_dmg(self, dmg):
        self.hp -= dmg

    def calc_dmg(self, target):
        # basic formula: atk minus target defense and armor
        dmg = self.atk - (target.dfn + target.armor)
        return max(0, dmg)

    def attack(self):
        if self.is_dead():
            return 0





class Player(Entity):
    def __init__(self, name, hp, atk, dfn, armor, is_dead, is_cursed, is_caught, tf_stage):
        super().__init__(name, hp, atk, dfn, armor, is_dead, is_cursed)
        self.tf_stage = 0
        self.is_caught = False

# Apply curse to player
    def apply_curse(self):
        self.is_cursed = True
        self.curse_level = 1
        print(f"You feel weird...")

class Enemy(Entity):
    def __init__(self, name, hp, atk, dfn, armor, is_dead, is_cursed):
        super().__init__(name, hp, atk, dfn, armor, is_dead, is_cursed)

class RegularMonster(Enemy):
    def __init__(self, name, hp, atk, dfn, armor, is_dead, is_cursed):
        super().__init__(name, hp, atk, dfn, armor, is_dead, is_cursed)

    def grab(self, target):
        pass


enemy1 = Enemy("Regular Monster", 50, 10, 10, 10, False, False)
enemy2 = Enemy("Squad Leader Monster", 75, 20, 20, 15, False, False)
enemy3 = Enemy("Elite Monster", 100, 30, 30, 30, False, False)
enemy4 = Enemy("Spy", 30, 5, 10, 0, False, False)
enemy5 = Enemy("Boss", 150, 50, 40, 45, False, False)















