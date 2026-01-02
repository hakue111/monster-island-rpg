from rpg.character.character import Character
from rpg.character.enemy_sheet import *
from rpg.item.weapon_sheet import *
from rpg.item.item_sheet import *
from rpg.magic.magic_sheet import *
import random


random_adj = ["Tricky", "Nutty", "Proud", "Slippery", "Dramatic", "Wooden", "Orange", "Special", "Wacky", "Jolly", "Angry", "Funny", "Big", "Lil'", "Horny"]
random_noun = ["Man", "Woman", "Robber", "Zombie", "Ghost", "Soldier", "Adventurer", "Dude", "Elf", "Mutant", "Thief", "Demon", "Monster"]


spells = [ice, ice_2, ice_3, fire, fire_2, fire_3, lightning, lightning_2, lightning_3, wind, wind_2, wind_3, water, water_2, water_3, darkness, flare, cure, cure_2, cure_3]

def enemy_generator():
    random_name = random.choice(random_adj) + "" + random.choice(random_noun)
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

    random_consumable = random.sample([potion, hi_potion, mega_potion, ether, hi_ether, mega_ether, elixir], k=random.randint(0,2))

    random_spell = []
    for _ in range(1, 3):
        spell_drawn = random.choice(spells)
        if spell_drawn in random_spell:
            continue
        if any ((spell_drawn.elemental == spell.elemental for spell in random_spell)):
            continue
        random_spell.append(spell_drawn)




    ytvwld: Enemy = Enemy("YtvwlD", random_hp, random_mp, random_elemental, random_weapon, [random_loot], random_xpdrop)
    ytvwld.set_stats(random_atk, random_def, random_matk, random_mdef, random_acc, random_eva)
    ytvwld.add_consumable(random_consumable)
    ytvwld.learn_spell(random_spell)

