from rpg.character.enemy_sheet import *
from rpg.item import weapon_sheet
from rpg.item.weapon_sheet import *
from rpg.item.item_sheet import *
from rpg.magic.magic_sheet import *
from rpg.item.weapon_randgen import *
import random

## NAME GEN
random_noun = ["Man", "Woman", "Robber", "Zombie", "Ghost", "Soldier", "Adventurer", "Dude", "Elf", "Mutant", "Thief", "Demon", "Monster", "Hacker", "Fucker", "Troll", "Clown", "Vampire", "Ogre", "Ghoul", "Alien", "Werewolf", "Doll", "Gorilla", "Fiend", "Kobold", "Gnome", "Sage", "Skeleton", "Robot"]
adj_tier1 = ["Regular", "Nutty", "Wooden", "Wacky", "Jolly", "Funny", "Lil'", "Boring"]
adj_tier2 = ["Proud", "Dramatic", "Creepy", "Angry", "Horny", "Tall", "Spooky"]
adj_tier3 = ["Professional", "Super", "Nightmarish", "Scary", "Special", "Big", "Evil"]

random_element = ["ice", "fire", "lightning", "wind", "water", "neutral", "darkness"]

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

weapons_tier1 = []
weapons_tier2 = []
weapons_tier3 = []
for name, variable in vars(weapon_sheet).items():
    if isinstance(variable, Weapon):
        if variable.tier == 1:
            weapons_tier1.append(variable)
        elif variable.tier == 2:
            weapons_tier2.append(variable)
        elif variable.tier == 3:
            weapons_tier3.append(variable)

items_tier1 = [potion, ether]
items_tier2 = [hi_potion, hi_ether]
items_tier3 = [mega_potion, mega_ether, elixir]


def randenemy_gen(tier: int):
    random_name: str
    random_hp: int
    random_mp: int
    random_elemental: str
    random_weapon: Weapon
    random_loot: list[ConsumableItem]
    random_xpdrop: int
    random_atk: int
    random_def: int
    random_matk: int
    random_mdef: int
    random_acc: int
    random_eva: int
    random_consumables: list[ConsumableItem]
    random_spells: list[Magic]

    if tier == 1:
        random_name = random.choice(adj_tier1) + " " + random.choice(random_noun)
        random_hp = random.randint(40,60)
        random_mp = random.randint(40,60)
        random_elemental = random.choice(random_element)
        random_weapon = randweapon_gen(1)
        random_loot = random.sample(items_tier1, k= random.randint(0,1))
        #make sure the random xpdrop is tied to overall stats and power
        random_xpdrop = random.randint(50,100)
        random_atk = random.randint(5,10)
        random_def = random.randint(5,10)
        random_matk = random.randint(5,10)
        random_mdef = random.randint(5,10)
        random_acc =random.randint(5,10)
        random_eva = random.randint(5,10)
        random_consumables = random.sample(items_tier1, k=1)
        random_spells = []
        for _ in range(0, 1):
            spell_drawn = random.choice(spells_tier1)
            if spell_drawn in random_spells:
                continue
            if any ((spell_drawn.elemental == spell.elemental for spell in random_spells)):
                continue
            random_spells.append(spell_drawn)

    elif tier == 2:
        random_name = random.choice(adj_tier2) + " " + random.choice(random_noun)
        random_hp = random.randint(61,90)
        random_mp = random.randint(61,90)
        random_elemental = random.choice(random_element)
        random_weapon = randweapon_gen(2)
        random_loot = random.sample(items_tier2, k= random.randint(0,1))
        #make sure the random xpdrop is tied to overall stats and power
        random_xpdrop = random.randint(101,150)
        random_atk = random.randint(5,10)
        random_def = random.randint(5,10)
        random_matk = random.randint(5,10)
        random_mdef = random.randint(5,10)
        random_acc =random.randint(5,10)
        random_eva = random.randint(5,10)
        random_consumables = random.sample(items_tier2, k=1)
        random_spells = []
        for _ in range(1, 2):
            spell_drawn = random.choice(spells_tier2)
            if spell_drawn in random_spells:
                continue
            if any ((spell_drawn.elemental == spell.elemental for spell in random_spells)):
                continue
            random_spells.append(spell_drawn)
    elif tier == 3:
        random_name = random.choice(adj_tier3) + " " + random.choice(random_noun)
        random_hp = random.randint(91, 120)
        random_mp = random.randint(91, 120)
        random_elemental = random.choice(random_element)
        random_weapon = randweapon_gen(3)
        random_loot = random.sample(items_tier3, k=random.randint(0, 2))
        # make sure the random xpdrop is tied to overall stats and power
        random_xpdrop = random.randint(151, 200)
        random_atk = random.randint(5, 10)
        random_def = random.randint(5, 10)
        random_matk = random.randint(5, 10)
        random_mdef = random.randint(5, 10)
        random_acc = random.randint(5, 10)
        random_eva = random.randint(5, 10)
        random_consumables = random.sample(items_tier3, k=1)
        random_spells = []
        for _ in range(2, 3):
            spell_drawn = random.choice(spells_tier3)
            if spell_drawn in random_spells:
                continue
            if any((spell_drawn.elemental == spell.elemental for spell in random_spells)):
                continue
            random_spells.append(spell_drawn)

    randenemy: Enemy = Enemy(
        random_name, random_hp, random_mp, random_elemental, random_weapon, [random_loot],
                             random_xpdrop)
    randenemy.set_stats(random_atk, random_def, random_matk, random_mdef, random_acc, random_eva)
    for item in random_consumables:
        randenemy.add_consumable(item, random.randint(0, 2), False)
    for spell in random_spells:
        randenemy.learn_spell(spell, False)

    return randenemy

# tests
if __name__ == "__main__":
    enemy1 = randenemy_gen(1)
    print(enemy1)
    print(enemy1.weapon)
    enemy1.print_consumables()
    enemy1.print_spells()

    enemy2 = randenemy_gen(2)
    print(enemy2)
    print(enemy2.weapon)
    enemy2.print_consumables()
    enemy2.print_spells()


    enemy3 = randenemy_gen(3)
    print(enemy3)
    print(enemy3.weapon)
    enemy3.print_consumables()
    enemy3.print_spells()
