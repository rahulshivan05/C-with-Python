// casino.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int play_game(int bet)
{
    srand(time(NULL));

    int num1 = rand() % 10;
    int num2 = rand() % 10;
    int num3 = rand() % 10;

    printf("Numbers: %d %d %d\n", num1, num2, num3);

    if (num1 == num2 && num2 == num3)
    {
        return bet * 10;
    }
    else if (num1 == num2 || num2 == num3 || num1 == num3)
    {
        return bet * 5;
    }
    else
    {
        return 0;
    }
}
