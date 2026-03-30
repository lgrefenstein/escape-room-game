# game data structure

# keys
key_a = "key_a"
key_b = "key_b"
key_c = "key_c"
key_d = "key_d"


# items
couch = {
    "name": "couch",
    "type": "item",
    "contains": None
}

piano = {
    "name": "piano",
    "type": "item",
    "contains": key_a
}

queen_bed = {
    "name": "queen bed",
    "type": "item",
    "contains": key_b
}

double_bed = {
    "name": "double bed",
    "type": "item",
    "contains": key_c
}

dresser = {
    "name": "dresser",
    "type": "item",
    "contains": key_d
}

dining_table = {
    "name": "dining table",
    "type": "item",
    "contains": None
}


# doors
door_a = {
    "name": "door_a",
    "type": "door",
    "key": key_a
}

door_b = {
    "name": "door_b",
    "type": "door",
    "key": key_b
}

door_c = {
    "name": "door_c",
    "type": "door",
    "key": key_c
}

door_d = {
    "name": "door_d",
    "type": "door",
    "key": key_d
}


# rooms
game_room = {
    "name": "Game Room",
    "type": "room",
    "items": [couch, piano],
    "doors": [door_a]
}

bedroom_1 = {
    "name": "Bedroom 1",
    "type": "room",
    "items": [queen_bed],
    "doors": [door_a, door_b, door_c]
}

bedroom_2 = {
    "name": "Bedroom 2",
    "type": "room",
    "items": [double_bed, dresser],
    "doors": [door_b]
}

living_room = {
    "name": "Living Room",
    "type": "room",
    "items": [dining_table],
    "doors": [door_c, door_d]
}

outside = {
    "name": "Outside",
    "type": "room",
    "items": [],
    "doors": [door_d]
}


# door connections
door_connections = {
    "door_a": [game_room, bedroom_1],
    "door_b": [bedroom_1, bedroom_2],
    "door_c": [bedroom_1, living_room],
    "door_d": [living_room, outside]
}


# game state
game_state = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside,
    "game_over": False
}