/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/1472/problem/A
/* Title  : Even-Odd Game
/* Notes  : tag-codeforces, tag-problem-D, tag-div-3
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
    ll n, c;
    cin >> n;

    vector<ll> v(n);

    for (ll &e : v) cin >> e;

    sort(v.begin(), v.end());

    ll sum = 0;

    forn(i, n) {
        c = v.back();
        v.pop_back();

        if (i % 2 == 0) {
            if (c % 2 == 0) sum += c;
        } else {
            if (c % 2 == 1) sum -= c;
        }
    }

    if (sum > 0) cout << "Alice";
    if (sum < 0) cout << "Bob";
    if (sum == 0) cout << "Tie";
}

int main() {
    IO();

    test() {
        #ifdef ONLINE_JUDGE
        solve();
        #else
        time__("Run duration: ") solve();
        #endif

        cout << endl;
    }

    return 0;
}