# player stats
player_hp = 100
player_atk = 20
player_dfn = 20
player_spd = 20
player_armor = 10

# enemy stats
enemy_hp = 100
enemy_atk = 10
enemy_dfn = 10
enemy_spd = 10
enemy_armor = 0


def win_lose():
    if player_hp <= 0:
        print("You lose! Game Over!")
    elif enemy_hp <= 0:
        print("Enemy defeated! You win!")




def player_attack():
    global enemy_hp
    choice = input("How do you want to attack? (punch)\n> ")
    if choice.casefold().strip() == "punch":
        dmg_calc = player_atk - (enemy_dfn + enemy_armor)
        enemy_hp -= max(0, dmg_calc)
        print(f"You punch the enemy!\n The enemy has {enemy_hp} HP left!")
    elif choice.casefold().strip() != "punch":
        print("Invalid input.")
        player_attack()


def enemy_attack():
    global player_hp
    dmg_calc = enemy_atk - (player_dfn + player_armor)
    player_hp -= max(0, dmg_calc)
    print(f"The enemy punches you!\n You have {player_hp} HP left!")






def start_fight():
    if player_spd >= enemy_spd:
        player_attack()
    while True:
        win_lose()
        enemy_attack()
        win_lose()
        player_attack()






start_fight()



























































