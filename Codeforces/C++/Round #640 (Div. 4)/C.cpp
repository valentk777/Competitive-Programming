/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/1352/problem/C
/* Title  : K-th Not Divisible by n
/* Notes  : tag-codeforces, tag-problem-C, tag-div-4
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <bits/stdc++.h>
/*----------------------------*/
using namespace std;
/*----------------------------*/
#define fast_cin()                    \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL)
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

#define test() \
    ll t;      \
    cin >> t;  \
    while (t--)
#define dbg(x) cout << #x << " = " << x << endl;

/*----------------------------*/

void IO() {
#ifndef ONLINE_JUDGE
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);
#endif
    fast_cin();
}

void solve() {
    ll n, k;
    cin >> n >> k;

    ll left = 1, right = 2 * k + 1, mid;

    while (left <= right) {
        mid = (left + right) / 2;
        ll check = (mid - mid / n);

        if (check < k) {
            left = mid;
        } else if (check > k) {
            right = mid;
        } else if (mid % n != 0) {
            cout << mid;
            break;
        } else {
            if ((mid + 1 - ((mid + 1) / n)) == k) {
                cout << mid + 1;
                break;
            } else {
                cout << mid - 1;
                break;
            }
        }
    }
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