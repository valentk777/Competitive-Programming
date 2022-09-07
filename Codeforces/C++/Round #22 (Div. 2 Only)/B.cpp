/*-----------------------------------------------------------*/
/* URL    : URL
/* Title  : TITLE
/* Notes  : tag-codeforces, tag-problem-B, tag-div-2
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

// https://codeforces.com/contest/22/problem/B
// #NotPass

void solve() {
    int n, m;
    cin >> n;
    cin >> m;

    string current;

    int a[n][m];
    int dp[n][m];

    forn(i, n) {
        cin >> current;
        forn(j, m) {
            a[i][j] = current[j] - '0';
        }
    }

    int x1, x2, y1, y2;

    forn(x1, n) {
        forn(y1, m) {
            if (a[x1][y1] == 0) {
                dp[x1][y1] = 1;
            } else {
                dp[x1][y1] = 0;
            }

            cout << dp[x1][y1] << " ";
        }
        cout << endl;
    }

        cout << endl;


    forn(x2, n) {
        forn(y2, m) {
            if (dp[x2][y2] == 0) {
                dp[x2][y2] = 0;
            } else if (x2 - 1 > -1 && y2 - 1 > -1) {
                dp[x2][y2] = 2* max(dp[x2 - 1][y2], dp[x2][y2 - 1]) - dp[x2-1][y2-1];
            } else if (x2 - 1 > -1) {
                dp[x2][y2] = dp[x2 - 1][y2] + 1;
            }
            else if (y2 - 1 > -1) {
                dp[x2][y2] = dp[x2][y2 - 1] +1;
            } else {
                dbg("x");
            }
            
            cout << dp[x2][y2] << " ";
        }
        cout << endl;
    }
}

int main() {
    IO();

    #ifdef ONLINE_JUDGE
    solve();
    #else
    time__("Run duration: ") solve();
    #endif

    return 0;
}