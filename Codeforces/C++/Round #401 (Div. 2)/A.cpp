/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/777/problem/A
/* Title  : A. Shell Game
/* Notes  : tag-codeforces, tag-problem-A, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <iostream>
using namespace std;

int n, x;

int main()
{
    cin >> n >> x;

    if (n % 6 == 0)
    {
        if (x == 0)
            return 0 * puts("0");
        if (x == 1)
            return 0 * puts("1");
        if (x == 2)
            return 0 * puts("2");
    }
    else if (n % 6 == 1)
    {
        if (x == 0)
            return 0 * puts("1");
        if (x == 1)
            return 0 * puts("0");
        if (x == 2)
            return 0 * puts("2");
    }

    else if (n % 6 == 2)
    {
        if (x == 0)
            return 0 * puts("1");
        if (x == 1)
            return 0 * puts("2");
        if (x == 2)
            return 0 * puts("0");
    }

    else if (n % 6 == 3)
    {
        if (x == 0)
            return 0 * puts("2");
        if (x == 1)
            return 0 * puts("1");
        if (x == 2)
            return 0 * puts("0");
    }
    else if (n % 6 == 4)
    {
        if (x == 0)
            return 0 * puts("2");
        if (x == 1)
            return 0 * puts("0");
        if (x == 2)
            return 0 * puts("1");
    }
    else if (n % 6 == 5)
    {
        if (x == 0)
            return 0 * puts("0");
        if (x == 1)
            return 0 * puts("2");
        if (x == 2)
            return 0 * puts("1");
    }
    return 0;
}