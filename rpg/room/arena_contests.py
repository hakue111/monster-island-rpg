from rpg.character.enemy_randgen import *

def contest_gen(tier: int) -> list[Enemy]:
    enemies = []
    names = []

    while len(enemies) < 5:
        enemy = randenemy_gen(tier)
        if enemy.name not in names:
            enemies.append(enemy)
            names.append(enemy.name)

    return enemies


# tests
if __name__ == "__main__":
    contestA = contest_gen(2)
    for enemy in contestA:
        print()
        print(enemy)
        print(enemy.weapon)
        print(enemy.consumables)
        print(enemy.spells)
        print()
      #  print(enemy.weapon)
       # enemy.print_spells()
        #enemy.print_consumables()
