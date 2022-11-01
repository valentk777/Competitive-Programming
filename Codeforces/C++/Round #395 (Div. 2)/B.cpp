/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/764/problem/B
/* Title  : B. Timofey and cubes
/* Notes  : tag-codeforces, tag-problem-B, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int z = 0;
bool q = true;

int main()
{
    cin >> n;
    int i = 0;
    vector<int> myVector;

    for (int i = 0; i < n; i++)
    {
        int k = 0;
        cin >> k;
        myVector.push_back(k);
    }

    if (n % 2 == 1)
    {
        for (int i = 0; i < n; i++)
        {

            if (q == true)
            {
                cout << myVector[n - i - 1] << " ";
                q = false;
            }
            else
            {
                q = true;
                cout << myVector[i] << " ";
            }
        }
    }
    else if (n < 5000)
    {
        for (int i = 0; i <= n - i + 1; i++)
        {
            // std::vector<int> myVector;
            // std::reverse(a.begin(), a.end());
            // reverse(a.begin(), a.end());
            reverse(myVector.begin() + i, myVector.end() - i);
        }

        for (int q = 0; q < n; q++)
        {
            cout << myVector[q] << " ";
        }
    }

    else
    {
        while (z < n / 2)
        {
            z += 1;

            if (q == true)
            {
                cout << myVector[n - i - 1] << " ";
                q = false;
            }
            else
            {
                q = true;
                cout << myVector[i] << " ";
            }
            i += 1;
        }

        q = false;

        while (z < n)
        {
            z += 1;

            if (q == true)
            {
                cout << myVector[n - i - 1] << " ";
                q = false;
            }
            else
            {
                q = true;
                cout << myVector[i] << " ";
            }
            i += 1;
        }
    }
    return 0;
}