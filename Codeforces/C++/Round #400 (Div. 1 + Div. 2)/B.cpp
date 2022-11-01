/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/776/problem/B
/* Title  : B. Sherlock and his girlfriend
/* Notes  : tag-codeforces, tag-problem-B, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <iostream>
#include <math.h>
using namespace std;

#define max 100005

int n;
int prime(int n);

int a[max];

int main()
{
    int k = 1;
    cin >> n;

    for (int i = 2; i < (n + 2); i++)
    {
        if (prime(i))
        {
            a[i - 2] = 1;
            continue;
        }
        else
        {
            a[i - 2] = 2;
            k = 2;
            continue;
        }
    }
    cout << k << endl;
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }

    return 0;
}

int prime(int n)
{
    bool isPrime = true;

    for (int i = 2; i <= sqrt(n); ++i)
    {
        if (n % i == 0)
        {
            isPrime = false;
            break;
        }
    }
    if (isPrime)
        return 1;
    else
        return 0;
}