/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/1472/problem/C
/* Title  : Long Jumps
/* Notes  : tag-codeforces, tag-problem-C, tag-div-3
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
#define max_arr(x, n) *max_element(x, x + n)
#define min_arr(x, n) *min_element(x, x + n)
#define max_vec(x) max_element(x.begin(), x.end())
#define min_vec(x) min_element(x.begin(), x.end())

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
    ll n;
    cin >> n;

    ll a[n], dp[n] = {};
    forn(i, n) {
        cin >> a[i];
    }

    rforn(i, n - 1) {
        if (i + a[i] < n) {
            dp[i] = a[i] + dp[i + a[i]];
        } else {
            dp[i] = a[i];
        }
    }

    cout << min_arr(dp, n) << endl;
}

int main() {
    IO();

    test() {
        #ifdef ONLINE_JUDGE
        solve();
        #else
        time__("Run duration: ") solve();
        #endif
    }

    return 0;
}