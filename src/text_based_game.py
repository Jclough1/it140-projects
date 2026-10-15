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
        print("You see:", rooms[current_room] ["item"]
    


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
