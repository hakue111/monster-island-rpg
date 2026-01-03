from rpg.item.weapon_sheet import *
from rpg.item.weapon import Weapon
import random

## NAME GEN
random_noun = ["Sword", "Bow", "Dagger", "Axe", "Claymore", "Club", "Whip", "Shuriken", "Saw", "Nunchucks"]
# TIER 1
random_adj1 = ["Regular", "Brand New", "Blue", "Green", "Red", "Purple", "Yellow", "White"]
# TIER 2
random_adj2 = ["Super", "Old", "Colorful", "Functional"]
# TIER 3
random_adj3 = ["Ultra", "Antique", "Black", "Premium", "Expert"]



def weapongen_t1():
    random_name = random.choice(random_adj1) + " " + random.choice(random_noun)
    random_dmg = random.randint(5, 10)
    random_value = random.randint(5, 10)
    randweapon_t1: Weapon = Weapon(random_name, random_dmg, random_value)
    print(randweapon_t1)

def weapongen_t2():
    random_name = random.choice(random_adj2) + " " + random.choice(random_noun)
    random_dmg = random.randint(11, 20)
    random_value = random.randint(11, 20)
    randweapon_t2: Weapon = Weapon(random_name, random_dmg, random_value)
    print(randweapon_t2)

def weapongen_t3():
    random_name = random.choice(random_adj3) + " " + random.choice(random_noun)
    random_dmg = random.randint(21, 30)
    random_value = random.randint(21, 30)
    randweapon_t3: Weapon = Weapon(random_name, random_dmg, random_value)
    print(randweapon_t3)


weapongen_t1()

weapongen_t2()

weapongen_t3()




