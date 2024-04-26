#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int rollDice()
{
    return rand() % 6 + 1;
}

int main()
{
    srand(time(NULL));

    int balance = 100; // Initial balance
    int bet;

    printf("Welcome to the Casino!\n");

    while (balance > 0)
    {
        printf("\nYour current balance: %d\n", balance);
        printf("Enter your bet (0 to quit): ");
        scanf("%d", &bet);

        if (bet == 0)
        {
            break;
        }

        if (bet > balance)
        {
            printf("Insufficient balance. Please place a lower bet.\n");
            continue;
        }

        int diceRoll = rollDice();
        printf("Dice roll: %d\n", diceRoll);

        if (diceRoll == 6)
        {
            printf("Congratulations! You won!\n");
            balance += bet;
        }
        else
        {
            printf("Sorry, you lost.\n");
            balance -= bet;
        }
    }

    printf("\nGame over. Your final balance: %d\n", balance);
    printf("Thank you for playing!\n");

    return 0;
}
