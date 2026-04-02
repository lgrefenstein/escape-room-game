# ---------- KEYS ----------
key_a = "key a"
key_b = "key b"
key_c = "key c"
key_d = "key d"


# ---------- ITEMS ----------
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


# ---------- DOORS ----------
door_a = {
    "name": "door a",
    "type": "door",
    "key": key_a,
    "connections": ["Game Room", "Bedroom 1"]
}

door_b = {
    "name": "door b",
    "type": "door",
    "key": key_b,
    "connections": ["Bedroom 1", "Bedroom 2"]
}

door_c = {
    "name": "door c",
    "type": "door",
    "key": key_c,
    "connections": ["Bedroom 1", "Living Room"]
}

door_d = {
    "name": "door d",
    "type": "door",
    "key": key_d,
    "connections": ["Living Room", "Outside"]
}


# ---------- ROOMS ----------
game_room = {
    "name": "Game Room",
    "type": "room",
    "items": ["couch", "piano"],
    "doors": ["door a"]
}

bedroom_1 = {
    "name": "Bedroom 1",
    "type": "room",
    "items": ["queen bed"],
    "doors": ["door a", "door b", "door c"]
}

bedroom_2 = {
    "name": "Bedroom 2",
    "type": "room",
    "items": ["double bed", "dresser"],
    "doors": ["door b"]
}

living_room = {
    "name": "Living Room",
    "type": "room",
    "items": ["dining table"],
    "doors": ["door c", "door d"]
}

outside = {
    "name": "Outside",
    "type": "room",
    "items": [],
    "doors": ["door d"]
}


# ---------- LOOKUPS ----------
all_items = {
    "couch": couch,
    "piano": piano,
    "queen bed": queen_bed,
    "double bed": double_bed,
    "dresser": dresser,
    "dining table": dining_table
}

all_doors = {
    "door a": door_a,
    "door b": door_b,
    "door c": door_c,
    "door d": door_d
}

all_rooms = {
    "Game Room": game_room,
    "Bedroom 1": bedroom_1,
    "Bedroom 2": bedroom_2,
    "Living Room": living_room,
    "Outside": outside
}


# ---------- GAME STATE ----------
game_state = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside,
    "game_over": False,
    "room_just_entered": True
}