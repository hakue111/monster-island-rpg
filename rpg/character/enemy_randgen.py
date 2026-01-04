from rpg.character.enemy_sheet import *
from rpg.item.weapon_sheet import *
from rpg.item.item_sheet import *
from rpg.magic.magic_sheet import *
import random

## NAME GEN
random_noun = ["Man", "Woman", "Robber", "Zombie", "Ghost", "Soldier", "Adventurer", "Dude", "Elf", "Mutant", "Thief", "Demon", "Monster", "Hacker"]
# TIER 1
random_adj1 = ["Regular", "Nutty", "Wooden", "Wacky", "Jolly", "Funny", "Lil'"]
# TIER 2
random_adj2 = ["Proud", "Dramatic", "Creepy", "Angry", "Horny", "Tall", "Spooky"]
# TIER 3
random_adj3 = ["Professional", "Super", "Nightmarish", "Scary", "Special", "Big"]

spells_tier1 = []
spells_tier2 = []
spells_tier3 = []
for name, variable in vars(magic_sheet).items():
    if isinstance(variable, Magic):
        if variable.tier == 1:
            spells_tier1.append(variable)
        elif variable.tier == 2:
            spells_tier2.append(variable)
        elif variable.tier == 3:
            spells_tier3.append(variable)

print(spells_tier1)
print(spells_tier2)
print(spells_tier3)

def enemy_generator(tier: int):
    if tier == 1:
        random_name = random.choice(random_adj1) + " " + random.choice(random_noun)
        random_hp = random.randint(40,60)
        random_mp = random.randint(30,120)
        random_elemental = random.choice(["ice", "fire", "lightning", "wind", "water", "neutral", "darkness"])
        random_weapon = random.choice([iron_sword, short_bow, dagger, fists, robot_claw, pincers, chuck_sword])
        random_loot = random.sample([potion, hi_potion, mega_potion, ether, hi_ether, mega_ether, elixir], k= random.randint(0,2))
        #make sure the random xpdrop is tied to overall stats and power
        random_xpdrop = random.randint(50,100)
        random_atk = random.randint(5,50)
        random_def = random.randint(5,50)
        random_matk = random.randint(5,50)
        random_mdef = random.randint(5,50)
        random_acc =random.randint(5,50)
        random_eva = random.randint(5,50)
        random_consumables = random.sample([potion, ether], k=random.randint(0,2))
        random_spells = []
        for _ in range(1, 3):
            spell_drawn = random.choice(spells_tier1)
            if spell_drawn in random_spells:
                continue
            if any ((spell_drawn.elemental == spell.elemental for spell in random_spells)):
                continue
            random_spells.append(spell_drawn)


        randenemy: Enemy = Enemy(random_name, random_hp, random_mp, random_elemental, random_weapon, [random_loot], random_xpdrop)
        randenemy.set_stats(random_atk, random_def, random_matk, random_mdef, random_acc, random_eva)
        for item in random_consumables:
            randenemy.add_consumable(item, random.randint(0,2), False)
        for spell in random_spells:
            randenemy.learn_spell(spell, False)




        print(randenemy)
        randenemy.print_consumables()
        randenemy.print_spells()

enemy_generator(2)