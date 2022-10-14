/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/630/problem/A
/* Title  : Again Twenty Five!
/* Notes  : tag-codeforces, tag-problem-A
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

/* 
NOTE:
if (0) -> True, 1 - False
x & 1 is equivalent to x % 2.
x >> 1 is equivalent to x / 2
*/

void IO() {
    #ifndef ONLINE_JUDGE
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);
    #endif
    fast_cin();
}

ll binpow_for_prime_m(ll a, ll n, ll mod) {
    n %= (mod - 1);

    ll res = 1;

    while(n > 0) {
        if (n & 1) {
            res = res * a % mod;
        }

        a = a * a % mod;
        n >>= 1;
    }

    return res;
}

ll binpow(ll a, ll n, ll mod) {
    ll res = 1;

    while(n > 0) {
        if (n & 1) {
            res = res * a % mod;
        }

        a = a * a % mod;
        n >>= 1;
    }

    return res;
}

void solve() {
    ll n;
    cin >> n;
    cout << 25; // for every number 5^n, when n >= 2 last two digints equal 25 :D 
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