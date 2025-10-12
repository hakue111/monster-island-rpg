from rpg import item_sheet, character
from rpg.character import Hero
from rpg.scene import Scene, SceneOptionDialogue, SceneOptionLambda, SceneOptionItem

boarding_scene: Scene = Scene("Boarding the Monster Island Ferry", "board")
boarding_scene.add_option(SceneOptionDialogue("You have won a free vacation on Monster Island."))
boarding_scene.add_option(SceneOptionDialogue(
    "You are standing on the docks. With your baggage and your ticket in your hands, you are about to board the ferry."))
boarding_scene.add_option(SceneOptionDialogue("Ferryman: What is your name?"))


def set_name():
    name_choice = input("@Player: Please enter your name and press Enter:\n> ")
    character.player = Hero(name_choice, 100)


boarding_scene.add_option(SceneOptionLambda(set_name))
boarding_scene.add_option(SceneOptionDialogue(
    f"Ferryman: So, you are {character.player.name}? Please board the ferry. We are departing soon."))
boarding_scene.add_option(SceneOptionDialogue(f"Ferryman: By the way, I have something useful for you."))
# give player a potion
boarding_scene.add_option(SceneOptionItem(item_sheet.potion, 5))
boarding_scene.add_option(SceneOptionDialogue(f"{character.player.name} boards the Ferry."))
boarding_scene.add_option(
    SceneOptionDialogue(f"The Ferry horn honks and the ship departs. Soon, the mainland will be out of sight."))
boarding_scene.add_option(
    SceneOptionDialogue(f"{character.player.name}, you are going on a dark and mysterious adventure. Be careful..."))
boarding_scene.add_option(SceneOptionDialogue("You arrive on Monster Island. You are greeted by the Mystery Man."))
boarding_scene.add_option(
    SceneOptionDialogue(f"Mystery Man: Welcome to Monster Island, {character.player.name}. Enjoy your stay..."))
