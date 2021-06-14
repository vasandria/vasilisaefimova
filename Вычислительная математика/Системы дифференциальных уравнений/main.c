#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main()
{
setlocale(LC_ALL, "");
double x = 2, y = 1, z = 1, t = 0;
double t2, h;
t2 = 2;
h = 0.1;
printf(" Крайнее значение t: %f ", t2);
printf(" Шаг: %f \n", h);

while(t < t2)
{
printf("t = %f  x = %f  y = %f  z = %f\n ", t, x, y, z);
x += (-2 * x + 5 * z) * h;
y += (sin(t - 1) * x - y - 3 * z) * h;
z += (-x + 2 * z) * h;

t += h;
}

    return 0;
}
