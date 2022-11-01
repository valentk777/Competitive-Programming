/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/779/problem/A
/* Title  : A. Pupils Redistribution
/* Notes  : tag-codeforces, tag-problem-A, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <bits/stdc++.h>
#include <iostream> // std::cout
#include <math.h>

using namespace std;

int n, input, k;
int A[6] = {0}, B[6] = {0};

int main()
{

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> input;
        if (input == 1)
            A[0] += 1;
        else if (input == 2)
            A[1] += 1;
        else if (input == 3)
            A[2] += 1;
        else if (input == 4)
            A[3] += 1;
        else
            A[4] += 1;
    }

    for (int i = 0; i < n; i++)
    {
        cin >> input;
        if (input == 1)
            B[0] += 1;
        else if (input == 2)
            B[1] += 1;
        else if (input == 3)
            B[2] += 1;
        else if (input == 4)
            B[3] += 1;
        else
            B[4] += 1;
    }

    for (int i = 0; i < 5; i++)
    {
        if (abs(A[i] - B[i]) % 2 != 0)
            return 0 * puts("-1");
        else
        {
            k += abs(A[i] - B[i]) / 2;
        }
    }
    cout << k / 2;
    return 0;
}