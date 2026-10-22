
# Jazmine Clough
# IT-140 Project Two: The Hangover in My House
# AI was used to help correct grammatical and indentation errors


def show_instructions():
    """Display the game instructions and available commands."""
    print("Welcome to The Hangover in My House!")
    print("Collect all 6 items before Drunk Neighbor Don catches you!")
    print("Move commands: go north, go south, go east, go west")
    print("Collect an item: get <item name>")
    print("To leave the game, type exit.")
    print("-" * 40)


def show_status(current_room, inventory, rooms):
    """Show the player's room, inventory, and available item."""
    print(f"\nYou are in the {current_room}.")
    print(f"Inventory: {inventory}")

    if "item" in rooms[current_room]:
        print(f"You see: {rooms[current_room]['item']}")

    print("-" * 40)


def main():
    """Run the text adventure game."""

    # Dictionary containing room connections and collectible items.
    rooms = {
        "Study Room": {
            "west": "Kitchen",
            "north": "Living Room"
        },
        "Kitchen": {
            "east": "Study Room",
            "north": "Theater Room",
            "item": "Food"
        },
        "Theater Room": {
            "south": "Kitchen",
            "north": "Bathroom",
            "east": "Living Room",
            "item": "Cell Phone Charger"
        },
        "Bathroom": {
            "south": "Theater Room",
            "east": "Basement",
            "item": "Shoes"
        },
        "Basement": {
            "west": "Bathroom",
            "east": "Bedroom",
            "south": "Living Room",
            "item": "Flashlight"
        },
        "Bedroom": {
            "west": "Basement",
            "south": "Dining Room",
            "item": "Blanket"
        },
        "Dining Room": {
            "north": "Bedroom",
            "west": "Living Room",
            "item": "Knife"
        },
        "Living Room": {
            "south": "Study Room",
            "west": "Theater Room",
            "north": "Basement",
            "east": "Dining Room"
        }
    }

    # Set the player's starting location and empty inventory.
    current_room = "Study Room"
    inventory = []
    required_items = 6
    villain_room = "Living Room"

    show_instructions()

    # Continue playing until the player wins, loses, or exits.
    while True:
        show_status(current_room, inventory, rooms)

        command = input("Enter your move: ").strip().lower()

        # Allow the player to leave the game.
        if command == "exit":
            print("You have exited the game.")
            print("Thanks for playing The Hangover in My House!")
            break

        # Process movement commands.
        elif command.startswith("go "):
            direction = command[3:].strip()

            if direction in ("north", "south", "east", "west"):
                if direction in rooms[current_room]:
                    current_room = rooms[current_room][direction]
                    print(f"You moved {direction}.")
                else:
                    print("You cannot go that direction.")
            else:
                print("Invalid direction. Please try again.")

        # Process item collection commands.
        elif command.startswith("get "):
            requested_item = command[4:].strip()
            room_item = rooms[current_room].get("item")

            if room_item and requested_item == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]["item"]
                print(f"You picked up the {room_item}!")
            else:
                print("That item is not available in this room.")

        # Handle incorrect commands.
        else:
            print("Invalid command. Please try again.")
            print("Use 'go north', 'get item name', or 'exit'.")

        # Check whether the player encountered the villain.
        if current_room == villain_room:
            print("\nDrunk Neighbor Don caught you!")
            print("GAME OVER! You lost!")
            print("Thanks for playing The Hangover in My House!")
            break

        # Check whether the player collected all six items.
        if len(inventory) == required_items:
            print("\nCongratulations!")
            print("You collected all 6 items and escaped safely!")
            print("YOU WIN!")
            print("Thanks for playing The Hangover in My House!")
            break


# Start the game.
if __name__ == "__main__":
    main()
    
