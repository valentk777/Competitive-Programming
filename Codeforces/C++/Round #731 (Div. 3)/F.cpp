/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/1547/problem/F
/* Title  : Array Stabilization (GCD version)
/* Notes  : tag-codeforces, tag-problem-f, tag-div-3
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

ll gcd(ll a, ll b) {
    return b == 0 ? a : gcd(b, a % b);
}

bool check_if_all_equal(const ll a[], ll n) {
    while (--n > 0 && a[n] == a[0])
        ;
    return n == 0;
}

void solve_to_slow() {
    ll n;
    cin >> n;

    ll a[n];

    forn(i, n) cin >> a[i];

    ll number = 0;
    bool all_equal = check_if_all_equal(a, n);

    while (!all_equal) {
        number++;

        ll first = a[0];
        all_equal = true;

        forn(i, n) {
            if (i + 1 != n) {
                a[i] = gcd(a[i], a[i + 1]);
            } else {
                a[i] = gcd(a[i], first);
            }

            if (i > 0 && all_equal && a[i] != a[i - 1]) {
                all_equal = false;
            }
        }
    }

    cout << number;
}

int main() {
    IO();

    test() {
#ifdef ONLINE_JUDGE
        solve_to_slow();
        #else
        time__("Run duration: ") solve_to_slow();
        #endif

        cout << endl;
    }

    return 0;
}