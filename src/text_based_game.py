"""Project Two starter for the student's text-based adventure game."""

# TODO: Add the full-name comment required by Project Two directions.


def show_instructions():
    """Display the game objective and available commands."""
print("The Hangover In My House")
print("Collect all 6 items before encountering Drunk Neighbor Don!")
print("Move commands: go north, go south, go east, go west")
print("Collect an item: get <item name")
print("-" * 40)

def show_status(current_room, inventory, rooms):
    """Display the player's location, Inventory, and available item."""
    print(f" \n You are in the {current_room}.")
    print(f"Inventory: {inventory}")
    if "item" in rooms[current_room]:
        print(f"You see:  {rooms[current_room] ['item']}")
    print("_" * 40)

def main():
    """Run the adventure game until the player wins or loses."""
    # Room connections and items follow the Project One game map.
    rooms = {
    "Study Room": {"west": "Kitchen", "north": "Living Room"},
    "Kitchen": {"east": "Study Room", "north": "Theater Room", "item": "Food"},
    "Theater Room": {"south": "Kitchen", "north": "Bathroom", "east": "Living Room", "item": "Cell Phone Charger"},
    "Bathroom": {"south": "Theater Room", "east": "Basement", "item": "Shoes"},
    "Basement": {"west": "Bathroom", "east": "Bedroom", "south": "Living Room", "item": "Flashlight"},
    "Bedroom":  {"west": "Basement", "south": "Dining Room", "item": "Blanket"},
    "Dining Room": {"north": "Bedroom", "west": "Living Room", "item": "Knife"},
    "Living Room": {"south": "Study Room", "west": "Theater Room", "north": "Basement", "east": "Dining Room"},
}

    current_room = "Study Room"
    inventory = []
    required_items = 6
    villain_room = "Living Room"

    show_instructions()

# Keep accepting commans until the player wins or loses.
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
    

    



    


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    # TODO: Show the current room.
    # TODO: Show the current inventory.
    # TODO: Show the current-room item when one is available.
    pass


def main():
    """Run the main gameplay loop."""
    # TODO: Create the full room/item dictionary from your Project One map.

    # TODO: Set the player's starting room.

    # TODO: Create the player's inventory.

    # TODO: Call the instruction function at the appropriate time.

    # TODO: Create the gameplay loop.
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    pass


if __name__ == "__main__":
    main()
