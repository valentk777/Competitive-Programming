/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/474/problem/B
/* Title  : Worms
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
    ll n, m, temp;
    cin >> n;

    ll a[n];

    cin >> temp;

    a[0] = temp;

    forsn(i, 1, n) {
        cin >> temp;
        a[i] = a[i - 1] + temp;
    }

    cin >> m;

    ll current, mid;

    forn(i, m) {
        ll left = 0, right = n;

        cin >> current;

        while (left <= right) {
            mid = (left + right) / 2;

            if (a[mid] < current) {
                left = mid;

            } else if (a[mid] > current && mid > 0 && a[mid - 1] + 1 > current) {
                right = mid;

            } else {
                break;
            }
        }

        cout << mid + 1 << endl;
    }
}

int main() {
    IO();

    #ifdef ONLINE_JUDGE
    solve();
    #else
    time__("Run duration: ") solve();
    #endif

    cout << endl;

    return 0;
}