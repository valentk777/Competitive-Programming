/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/776/problem/A
/* Title  : A. A Serial Killer
/* Notes  : tag-codeforces, tag-problem-A, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string a, b, c;
    int n;

    cin >> a >> b;
    cin >> n;

    cout << a << " " << b << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> c;
        if (c == a)
        {
            cin >> a;
            cout << a << " " << b << endl;
        }
        else
        {
            cin >> b;
            cout << a << " " << b << endl;
        }
    }

    return 0;
}