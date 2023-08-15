#!/usr/bin/python3

# Script Written by: Calise Wall 

# function to show the game instructions
def show_instructions():
    print("Welcome to Escape from the Enchanted Forest!")
    print("Shadow Keeper vs You")
    print("Collect all 6 Gemstones, defeat the Shadowy Lair! and win the game!!!")
    print("Move commands for directions: North, South, East, West")
    print("")

# Define the rooms and their connections
rooms = {
    "Start Room": {"North": "Whispering Trees", "East": "Magical Clearing"},
    "Whispering Trees": {"South": "Start Room", "West": "Crystal Cave"},
    "Magical Clearing": {"West": "Start Room"},
    "Crystal Cave": {"East": "Whispering Trees", "South": "Moonlit Grove"},
    "Enchanted Waterfall": {"South": "Gloomy Glen"},
    "Gloomy Glen": {"North": "Enchanted Waterfall"},
    "Moonlit Grove": {"North": "Crystal Cave", "West": "Shadowy Lair"},
    "Shadowy Lair": {"East": "Moonlit Grove"}
}

# Define the items in each room
initial_items = {
    "Whispering Trees": "Gemstone 2",
    "Magical Clearing": "Gemstone 1",
    "Crystal Cave": "Gemstone 3",
    "Enchanted Waterfall": "Gemstone 4",
    "Gloomy Glen": "Gemstone 5",
    "Moonlit Grove": "Gemstone 6",
}

# Define the villain's room
villain_room = "Shadowy Lair"

# Player's inventory to store collected gemstones
inventory = []

# function to get the new state based on player's input
def get_new_state(current_state, direction):
    if current_state in rooms and direction in rooms[current_state]:
        return rooms[current_state][direction]
    return current_state

# function to show the player's status
def show_status(state):
    print("You are in the", state)
    print("Inventory:", inventory)
    print("")

def play_game():
    current_room = "Start Room"

    while True:
        show_status(current_room)

        command = input("Enter 1 to move to another room, or 2 to collect item from the current room: ")

        if command == "1":
            direction = input(f"Enter direction ({', '.join(rooms[current_room].keys())}): ").capitalize()
            current_room = get_new_state(current_room, direction)
        elif command == "2":
            if current_room in initial_items:
                item = initial_items[current_room]
                print(f"You collected {item}.")
                inventory.append(item)
                del initial_items[current_room]  # Remove the gemstone from the room
            else:
                print("There is no item to collect in this room.")
        else:
            print("Invalid command. Please try again.")

        if current_room == villain_room:
            print("Oh no! You encountered the Shadow Keeper! Game Over.")
            break

        if len(inventory) == len(initial_items):
            print("Congratulations! You collected all the gemstones and escaped from the Enchanted Forest!")
            break

if __name__ == "__main__":
    show_instructions()
    play_game()
