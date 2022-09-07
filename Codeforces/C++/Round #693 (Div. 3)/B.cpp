/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/1472/problem/A
/* Title  : Fair Division
/* Notes  : tag-codeforces, tag-problem-B, tag-div-3
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <bits/stdc++.h>
/*----------------------------*/
using namespace std;
/*----------------------------*/
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define debug(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
#define time__(d) for (auto blockTime = make_pair(chrono::high_resolution_clock::now(), true); blockTime.second; debug("%s: %d ms\n", d, (int)chrono::duration_cast<chrono::milliseconds>(chrono::high_resolution_clock::now() - blockTime.first).count()), blockTime.second = false)
/*----------------------------*/
#define ll long long int
typedef long double ld;
/*----------------------------*/
#define forn(i, e) for (ll i = 0; i < e; i++)
#define forsn(i, s, e) for (ll i = s; i < e; i++)
#define rforn(i, s) for (ll i = s; i >= 0; i--)
#define rforsn(i, s, e) for (ll i = s; i >= e; i--)

#define test() ll t; cin >> t; while (t--)
#define dbg(x) cout<<#x<<" = "<<x<<endl;

/*----------------------------*/

void IO() {
    #ifndef ONLINE_JUDGE
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);
    #endif
    fast_cin();
}

void solve() {
    int n, current;
    cin >> n;

    int c;

    int sum1 = 0, sum2 = 0;
    forn(i, n) {
        cin >> c;
        if (c == 1)
            sum1++;
        else
            sum2 += 2;
    }

    if ((sum1 + sum2) % 2 != 0)
        cout << "NO";
    else if (sum1 >= 2 || (sum2 / 2) % 2 == 0)
        cout << "YES";
    else
        cout << "NO";
}

int main() {
    IO();

    test() {
        #ifdef ONLINE_JUDGE
        solve();
        cout << endl;
        #else
        time__("Run duration: ") solve();
        cout << endl;
        #endif
    }

    return 0;
}