"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}



current_room = "Great Hall"
# Display Game Instructions.
print("Welcome to the Easy Dragon Text Game!")
print("Move between rooms using go north, south, east, or west.")
print("Type 'exit' to leave the game.")

#Continue playing unitl the player exits.
while current_room != "exit":
    
#Display the player's current location.
    print("\nYou are in the", current_room)

    #Ask the player for a command.
    command = input("Enter your move:").strip().lower()

    #Check whether the player wants to exit.
    if command == "exit":
        current_room = "exit"

#check whether the player entered a movement command.
    elif command.startswith("go "):
        direction = command[3:].strip()

    #Move only if the direction is available.
        if direction in rooms[current_room]:
           current_room = rooms [current_room][direction]
           print("You moved", direction)

        else: 
           print("Invalid direction. You cannot go that way.")

# Handle any other invalid command.

    else:
        print("Invalid command. Use 'go north', 'go south'",)
        print("go east', 'go west', or 'exit'.")

#End the game
print("Thank you for playing! Goodbye!")
    



