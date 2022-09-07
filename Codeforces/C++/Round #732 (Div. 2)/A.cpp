/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/1546/problem/A
/* Title  : AquaMoon and Two Arrays
/* Notes  : tag-codeforces, tag-problem-A, tag-div-2
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

    ll sum_a = 0, sum_b = 0;
    ll a[n], b[n], c[n];

    forn(i, n) {
        cin >> a[i];
        sum_a += a[i];
    }

    forn(i, n) {
        cin >> b[i];
        sum_b += b[i];
    }

    if (sum_a % 2 == 0 && sum_b % 2 == 1 || sum_a % 2 == 1 && sum_b % 2 == 0) {
        cout << -1 << endl;
        return;
    }

    if (n == 1) {
        if (a[0] != b[0]) {
            cout << -1 << endl;
            return;
        } else {
            cout << 0 << endl;
            return;
        }
    }

    forn(i, n) c[i] = a[i] - b[i];

    vector<string> r;
    int count = 0;

    ll max_e = 0, min_e = 1;

    while (max_e != 0 || min_e != 0) {
        max_e = max_arr(c, n);
        min_e = min_arr(c, n);

        int pmax = distance(c, max_element(c, c + n));
        int pmin = distance(c, min_element(c, c + n));
        while (c[pmax] != 0 && c[pmin] != 0) {
            c[pmax]--;
            c[pmin]++;
            count++;
            r.push_back(to_string(pmax + 1) + " " + to_string(pmin + 1));
        }
    }

    cout << count << endl;
    for (string i : r) cout << i << endl;
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