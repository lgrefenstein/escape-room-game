import time

from data import all_items, all_doors, all_rooms


def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def start_game(game_state):
    slow_print("Welcome to the Escape Room Game!\n")

    slow_print(
        "You are a student at Ironhack Bootcamp.\n"
        "It's been another brutal day of coding — loops, functions, staring at a screen.\n"
        "Your eyes burned. You dropped onto the couch with your laptop still open...\n"
    )
    time.sleep(1)

    slow_print("...and fell fast asleep zZzZzZ\n")
    time.sleep(1)

    slow_print(
        "Now you're waking up.\n"
        "The door is locked. Your phone is gone...\n"
    )

    slow_print("Find the keys, unlock the doors, and escape the house!\n")

    while not game_state["game_over"]:
        if game_state["current_room"] == game_state["target_room"]:
            slow_print("Congratulations! You escaped the house!")
            game_state["game_over"] = True
        else:
            game_state = play_room(game_state)


def explore_room(room):
    slow_print("In this room you see:\n")

    for item in room["items"]:
        print(f"- {item.title()}")

    for door in room["doors"]:
        print(f"- {door.title()}")

    print()


def examine_item(item_name, game_state):
    current_room = game_state["current_room"]

    if item_name not in all_items:
        slow_print("This item does not exist.")
        return

    if item_name not in current_room["items"]:
        slow_print("This item is not in this room.")
        return

    item = all_items[item_name]
    key = item["contains"]

    if key:
        if key not in game_state["keys_collected"]:
            slow_print(f"You found {key.title()}!")
            game_state["keys_collected"].append(key)
        else:
            slow_print("You already have that key!")
    else:
        slow_print("There's nothing here...")


def show_inventory(game_state):
    if not game_state["keys_collected"]:
        slow_print("You do not have any keys yet.")
    else:
        slow_print("Keys collected:")
        for key in game_state["keys_collected"]:
            slow_print(f"- {key.title()}")


def unlock_door(door_name, game_state):
    current_room = game_state["current_room"]

    if door_name not in current_room["doors"]:
        slow_print("This door is not in this room.")
        return False

    door = all_doors[door_name]
    required_key = door["key"]

    if required_key in game_state["keys_collected"]:
        slow_print("Success! You unlocked the door.")
        return True

    slow_print("The door is locked. You don't have the key yet.")
    return False


def go_to_next_room(door_name, game_state):
    current_room_name = game_state["current_room"]["name"]
    door = all_doors[door_name]

    for room_name in door["connections"]:
        if room_name != current_room_name:
            game_state["current_room"] = all_rooms[room_name]
            game_state["room_just_entered"] = True
            slow_print(f"\nYou go through {door_name.title()} and enter {room_name}.")
            return


def play_room(game_state):
    current_room = game_state["current_room"]

    if game_state["room_just_entered"]:
        slow_print(f"\nYou are in the {current_room['name']}.\n")
        explore_room(current_room)
        game_state["room_just_entered"] = False

    player_input = input(
        "What do you want to do?\n"
        'Type an item, a door, or "inventory": '
    ).strip().lower()

    print()

    if player_input == "inventory":
        show_inventory(game_state)

    elif player_input in current_room["items"]:
        examine_item(player_input, game_state)

    elif player_input in current_room["doors"]:
        if unlock_door(player_input, game_state):
            go_to_next_room(player_input, game_state)

    else:
        slow_print("Invalid input. Please type something from the room.")

    return game_state