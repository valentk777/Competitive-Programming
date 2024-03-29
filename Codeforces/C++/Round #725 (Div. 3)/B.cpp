/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/1538/problem/B
/* Title  : Friends and Candies
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
#define dbg(x) cout<<#x<<" = "<<x<<ln

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

    ll i, a[n + 1], sum = 0, ans = 0;

    forn(i, n) {
        cin >> a[i];
        sum += a[i];
    }

    if (sum % n != 0) {
        cout << -1 << endl;
        return;
    }

    sum /= n;

    forn(i, n) {
        if (a[i] > sum)
            ans++;
    }

    cout << ans << endl;
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