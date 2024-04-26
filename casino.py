import ctypes

# Load the shared library
casino = ctypes.CDLL('./casino.so')  # Update the path if necessary

# Define the argument and return types of the function
casino.play_game.argtypes = (ctypes.c_int,)
casino.play_game.restype = ctypes.c_int

# Get the user's bet from input
bet = int(input("Enter your bet: "))

# Call the C function
winnings = casino.play_game(bet)

# Print the result
if winnings > 0:
    print(f"You won {winnings}!")
else:
    print("Sorry, you lost.")
