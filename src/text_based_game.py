"""Project Two starter for the student's text-based adventure game."""


# TODO: Add the full-name comment required by Project Two directions.
# Jazmine Clough

def show_instructions():
    """Display the game objective and available commands."""
    # TODO:
    print("The Hangover in my house")
    print("Collect all 6 items without entering the living room")
    print("Move commands:go north, go south, go east, go west")
    print("Collect items: get item name")
    
    


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("You are in the", current_room)
    
   # Show the current inventory.
    print("Inventory:", inventory)
    
    # TODO: Show the current-room item when one is available.
    if "item" in rooms[current_room]:
        print("You see:", rooms[current_room] ["item"])
    


def main():
    """Run the main gameplay loop."""
    # TODO: Create the full room/item dictionary from your Project One map.
    rooms = {
        "Study Room": {"west": "Kitchen", "north": "Living Room"}
    }
    current_room = "Study Room"

    inventory = []
    show_instructions()
    while True:
        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip().lower()

        if command.startswith("go "):
            direction = command[3:].strip()
            if direction in rooms[current_room]:
                current_room = rooms[current_room] [direction]
                print(f"You moved {direction}.")

            else:
                 print("You cannot go that direction. Please try again.")

        elif command.startswith("get "):
            requested_item = command[4:].strip()
            room_item = rooms[current_room].get("item")
            if room_item and requested_item == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room] ["item"]
                print(f"You picked up the {room_item}!")

            else:
                print("That item is not available in this room.")

        else:
            print("Invalid command. Use 'go north' or 'get item name'.")


    

 


if __name__ == "__main__":
    main()
