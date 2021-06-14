#include<math.h>
#include<stdio.h>

double func(double x, double y, double z)
{
	return y + z / x;
}
double func1(double x, double y, double z)
{
	return z;
}

void main()
{
	double K1, K2, K3, K4, Q1, Q2, Q3, Q4, h = 0.1, a = 1, b = 1.5, x = a, y = 0.77, z = -0.44, z0, y0;

	while (x < b + h)

	{
	    K1 = h * func(x, y, z);
        Q1 = h * func1(x, y, z);

        K2 = h * func(x + h / 2.0, y + Q1 / 2.0, z + K1 / 2.0);
        Q2 = h * func1(x + h / 2.0, y + Q1 / 2.0, z + K1 / 2.0);

        K3 = h * func(x + h / 2.0, y + Q2 / 2.0, z + K2 / 2.0);
        Q3 = h * func1(x + h / 2.0, y + Q2 / 2.0, z + K2 / 2.0);

        K4 = h * func(x + h, y + Q3, z + K3);
        Q4 = h * func1(z + h, y + Q3, z + K3);


        z0 = z - (K1 + 2.0 * K2 + 2.0 * K3 + K4) / 6.0;
        y0 = y + (Q1 + 2.0 * Q2 + 2.0 * Q3 + Q4) / 6.0;


        printf("x = %f, ", x);
        printf(" y = %f, ", y0);
        printf(" z = %f \n", z0);

        y = y0;
        z = z0;
        x += h;

	}
return 0;
}
