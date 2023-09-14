def print_my_name(name):
    print(name)

print_my_name('Bob')

def trip_planner(start, end, duration, mode = 'car'):
    print(f"It looks like you're starting your trip from {start}")
    print(f"You are planning to get to {end}")
    print(f"It should take you about {duration} hours")
    print(f"I see you are taking a {mode}")

trip_planner('Paradigm', 'Disneyland', 2, 'plane')