/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/766/problem/A
/* Title  : A. Mahmoud and Longest Uncommon Subsequence
/* Notes  : tag-codeforces, tag-problem-A, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string a, b;

    cin >> a;
    cin >> b;

    if (a == b)
        return 0 * puts("-1");

    int al, bl;
    al = a.length();
    bl = b.length();
    if (al >= bl)
    {
        cout << al;
        return 0;
    }
    if (al <= bl)
    {
        cout << bl;
        return 0;
    }
}