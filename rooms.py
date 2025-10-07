# goals:
# 1. modeling the interior of a room
# 2. taking input from a user to go places / get items
#    * also handling bad input
# 3. tracking player location
# 4. player inventory
# 5. victory / loss conditions


inventory = []

current_room = "Island Docks"

rooms = {
    "Island Docks" : {
                "north": "Carnival"
    },
    "Carnival": {
                "north": "Forest",
                "west": "Hotel",
                "east": "The Bar",
                "south": "Island Docks"
    }
}

print("You are in the", current_room)