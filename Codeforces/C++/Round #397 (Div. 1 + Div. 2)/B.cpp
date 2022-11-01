/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/765/problem/B
/* Title  : B. Code obfuscation
/* Notes  : tag-codeforces, tag-problem-B, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <iostream>

using namespace std;
char s[503];
int main()
{
    int x = 'a';
    cin >> s;
    for (int i = 0; s[i]; i++)
    {
        if (s[i] > x)
        {
            cout << "NO";
            return 0;
        }
        x += (s[i] == x);
    }
    cout << "YES";
    return 0;
}