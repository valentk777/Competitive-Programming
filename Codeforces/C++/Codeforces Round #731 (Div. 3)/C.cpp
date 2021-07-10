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
    ll k, n, m;
    cin >> k >> n >> m;

    ll a[n], b[m];

    forn(i, n) cin >> a[i];
    forn(i, m) cin >> b[i];

    ll ai = 0, bi = 0;
    ll r[n + m];

    forn(i, n + m) {
        if (ai < n && a[ai] == 0) {
            r[i] = a[ai];
            ai++;
            k++;
        } else if (bi < m && b[bi] == 0) {
            r[i] = b[bi];
            bi++;
            k++;
        } else if (ai < n && a[ai] <= k) {
            r[i] = a[ai];
            ai++;
        } else if (bi < m && b[bi] <= k) {
            r[i] = b[bi];
            bi++;
        } else {
            cout << -1;
            return;
        }
    }

    forn(i, n + m) cout << r[i] << " ";
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