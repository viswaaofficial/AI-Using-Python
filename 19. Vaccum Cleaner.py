class VacuumCleaner:
    def __init__(self, start_position, room_states):
        self.state = (start_position, *room_states)

    def clean(self):
        position, *rooms = self.state
        if rooms[position] == 1:
            rooms[position] = 0
        self.state = (position, *rooms)

    def move(self, direction):
        position, *rooms = self.state
        if direction == "left" and position > 0:
            position -= 1
        elif direction == "right" and position < len(rooms) - 1:
            position += 1
        self.state = (position, *rooms)

    def display_state(self):
        position, *rooms = self.state
        room_status = ['Clean' if state == 0 else 'Dirty' for state in rooms]
        print(f"Position: Room {position + 1}, " + ", ".join([f"Room {i+1}: {status}" for i, status in enumerate(room_status)]))

# Example usage
start_position = int(input("Enter starting position (0 for Room A, 1 for Room B, etc.): "))
room_states = list(map(int, input("Enter room states (0 for clean, 1 for dirty), separated by space: ").split()))

vacuum = VacuumCleaner(start_position, room_states)

# Initial state display
print("Initial State:")
vacuum.display_state()

# Dynamic actions
while any(room_state == 1 for room_state in vacuum.state[1:]):
    if vacuum.state[1 + vacuum.state[0]] == 1:
        vacuum.clean()
    else:
        vacuum.move("right" if vacuum.state[0] < len(vacuum.state) - 2 else "left")
    vacuum.display_state()

# Final state display
print("\nFinal State:")
vacuum.display_state()
