from ex47.game import Room

def test_room():
    gold = Room("GoldRoom", "Room with gold.")
    assert gold.name == "GoldRoom"
    assert gold.paths == {}

def test_room_paths():
    center = Room("Center", "Central room")
    north = Room("North", "North room")
    south = Room("South", "South room")

    center.add_paths({'north': north, 'south': south})
    assert center.go('north') == north
    assert center.go('south') == south
