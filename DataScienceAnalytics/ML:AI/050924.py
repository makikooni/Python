def are_doors_open(door_a, door_b):
    # The doors open if (Door A is unlocked) OR (Door B is locked)
    return door_a or not door_b
 
# Test all possible combinations of 2 doors being locked or unlocked
def test_all_possibilities():
    print("Door statuses (A, B) and if all doors open:")
 
    # Possible combinations (True = unlocked, False = locked)
    possibilities = [
        (True, True),    # A = Unlocked, B = Unlocked
        (True, False),   # A = Unlocked, B = Locked
        (False, True),   # A = Locked, B = Unlocked
        (False, False)   # A = Locked, B = Locked
    ]
    
    for doors in possibilities:
        door_a, door_b = doors
        print(f"A = {'Unlocked' if door_a else 'Locked'}, B = {'Unlocked' if door_b else 'Locked'} -> Doors open? {are_doors_open(door_a, door_b)}")
 
# Run the test for all possibilities
test_all_possibilities()