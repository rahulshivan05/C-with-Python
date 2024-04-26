#include <stdio.h>

void multiply_array(int *array, int lenght, int scalar)
{
    for (int i = 0; i < lenght; i++)
    {
        array[i] *= scalar;
    }
}