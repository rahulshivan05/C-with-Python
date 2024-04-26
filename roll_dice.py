import ctypes

# Load the shared library
casino = ctypes.CDLL('./roll_dice.so')  # Update the path if necessary

# Define the C function prototype
casino.rollDice.restype = ctypes.c_int


def roll_dice():
    return casino.rollDice()


def play_game():
    balance = 100  # Initial balance

    print("Welcome to the Casino!")

    while balance > 0:
        print("\nYour current balance:", balance)
        bet = int(input("Enter your bet (0 to quit): "))

        if bet == 0:
            break

        if bet > balance:
            print("Insufficient balance. Please place a lower bet.")
            continue

        dice_roll = roll_dice()
        print("Dice roll:", dice_roll)

        if dice_roll == 6:
            print("Congratulations! You won!")
            balance += bet
        else:
            print("Sorry, you lost.")
            balance -= bet

    print("\nGame over. Your final balance:", balance)
    print("Thank you for playing!")


if __name__ == '__main__':
    play_game()
