from rpg.item.weapon_sheet import *
from rpg.item.weapon import Weapon
import random

## NAME GEN
random_noun = ["Sword", "Bow", "Dagger", "Axe", "Claymore", "Club", "Whip", "Shuriken", "Saw", "Nunchucks"]
# TIER 1
random_adj1 = ["Regular", "Old", "Everyday", "Rusty", "Used"]
# TIER 2
random_adj2 = ["Super", "Brand New", "Functional", "Cool", "Red", "Orange", "Yellow" "Green", "Blue", "Indigo", "Violet"]
# TIER 3
random_adj3 = ["Ultra", "Antique", "Black", "Premium", "Professional", "Heavy"]



def randweapon_gen(tier: int):
    if tier == 1:
        random_name = random.choice(random_adj1) + " " + random.choice(random_noun)
        random_dmg = random.randint(5, 10)
        random_value = random.randint(25, 50)
        randweapon_t1: Weapon = Weapon(random_name, random_dmg, random_value, tier)
        print(randweapon_t1)
    elif tier == 2:
        random_name = random.choice(random_adj2) + " " + random.choice(random_noun)
        random_dmg = random.randint(11, 20)
        random_value = random.randint(51, 100)
        randweapon_t2: Weapon = Weapon(random_name, random_dmg, random_value, tier)
        print(randweapon_t2)
    elif tier == 3:
        random_name = random.choice(random_adj3) + " " + random.choice(random_noun)
        random_dmg = random.randint(21, 30)
        random_value = random.randint(101, 150)
        randweapon_t3: Weapon = Weapon(random_name, random_dmg, random_value, tier)
        print(randweapon_t3)


#randweapon_gen(random.randint(1, 3))




#def weapongen_t2():
 #   random_name = random.choice(random_adj2) + " " + random.choice(random_noun)
  #  random_dmg = random.randint(11, 20)
   # random_value = random.randint(11, 20)
    #randweapon_t2: Weapon = Weapon(random_name, random_dmg, random_value)
    #print(randweapon_t2)

#def weapongen_t3():
#    random_name = random.choice(random_adj3) + " " + random.choice(random_noun)
#    random_dmg = random.randint(21, 30)
#    random_value = random.randint(21, 30)
#    randweapon_t3: Weapon = Weapon(random_name, random_dmg, random_value)
 #   print(randweapon_t3)