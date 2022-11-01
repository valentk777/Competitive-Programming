/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/765/problem/C
/* Title  : C. Table Tennis Game 2
/* Notes  : tag-codeforces, tag-problem-C, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <iostream>
#include <math.h>
using namespace std;

int gcd(int a, int b)
{
    return b == 0 ? a : gcd(b, a % b);
}

int division(int a, int b)
{
    return a / b;
}

int skaicius(int k, int g)
{
    int bendras = gcd(k, g);
    k = division(k, bendras);
    g = division(g, bendras);

    return division(g, k);
}

int main()
{
    int k, a, b;
    cin >> k >> a >> b;

    if (k > a && k > b)
        return 0 * puts("-1");
    if ((k > a && b % k != 0) || (k > b && a % k != 0))
        return 0 * puts("-1");

    cout << skaicius(k, a) + skaicius(k, b) << endl;
}