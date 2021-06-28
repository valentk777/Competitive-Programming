/*-------- valentk777 --------*/
#include <bits/stdc++.h>
// #include <map>
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
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    fast_cin();
}

void solve() {
    ll n;
    cin >> n;

    ll a[n], prev[n], dp[n] = {};

    forn(i, n) {
        cin >> a[i];
    }

    int last = 0;

    forn(i, n) {
        dp[i] = 1;
        prev[i] = -1;

        forn(j, i) {
            if (a[j] < a[i] && dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
                last = i;
            }
        }
    }

    int current = last;

    /*---------- using arrays ------------------*/

    int temp[n] = {};
    int nn = 0;

    while(current >=0) {
        temp[nn] = current;
        nn++;
        current = prev[current];
    }

    rforn(i, nn - 1) {
        cout << a[temp[i]] << " ";
    }

    /*---------- using vectors ------------------*/

    vector<int> v;

    while(current >=0) {
        v.push_back(a[current]);
        current = prev[current];
    }

    reverse(v.begin(), v.end());
    for(auto e : v) cout << e << " ";
}

int main() {
    IO();

    test() {
        time__("Run duration: ") solve();
        cout << endl;
    }

    return 0;
}