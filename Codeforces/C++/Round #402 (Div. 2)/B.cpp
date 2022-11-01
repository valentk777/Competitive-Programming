/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/779/problem/B
/* Title  : B. Weird Rounding
/* Notes  : tag-codeforces, tag-problem-B, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <iostream> // std::cout
#include <math.h>
#include <string>
#include <stdio.h>

#define max 2000000005

using namespace std;

int main()
{

    int k, i = 0, j, h = 0, trinti = 0;
    string n;

    cin >> n >> k;
    j = n.length();

    for (int i = 1; i <= j; i++)
    {

        if (n[j - i] == '0')
        {
            h += 1;
            if (h == k)
            {
                cout << trinti;
                return 0;
            }
        }
        else
        {
            trinti += 1;
        }
    }
    cout << j - 1;

    return 0;
}