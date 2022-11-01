/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/779/problem/C
/* Title  : C. Dishonest Sellers
/* Notes  : tag-codeforces, tag-problem-C, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <iostream> // std::cout
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

    int n, k, input, suma = 0;

    cin >> n >> k;
    vector<int> a;
    for (int i = 0; i < n; i++)
    {
        cin >> input;
        a.push_back(input);
        suma += input;
    }

    vector<int> b;
    for (int i = 0; i < n; i++)
    {
        cin >> input;
        b.push_back(a[i] - input);
    }

    sort(b.begin(), b.end());

    for (int i = 0; i < n; i++)
    {

        if (i >= k && b[i] > 0)
        {
            suma -= b[i];
        }
    }
    cout << suma;

    return 0;
}