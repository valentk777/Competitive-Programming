/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/782/problem/A
/* Title  : A. Andryusha and Socks
/* Notes  : tag-codeforces, tag-problem-A, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
// valentk777

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>

using namespace std;
typedef long long ll;

#define fori(n);    for(int i = 0; i<n; i++)
#define fork(n);    for(int k = 0; k<n; k++)
#define forj(n);    for(int j = 0; j<n; j++)
#define fori1(n);   for(int i = 1; i<=n; i++)
#define fork1(n);   for(int k = 1; k<=n; k++)
#define forj1(n);   for(int j = 1; j<=n; j++)

#define max 200005

ll n, k;
int a[max] = {0};
int maxim = 0;
int suma = 0;

int main()
{
    cin >> n
               fori(2 * n)
    {
        cin >> k;
        if (a[k - 1] == 0)
        {
            a[k - 1] = 1, suma += 1;
            if (suma > maxim)
                maxim = suma;
        }
        else
        {
            a[k - 1] = 0, suma -= 1;
            if (suma > maxim)
                maxim = suma;
        }
    }

    cout << maxim;
    return 0;
}