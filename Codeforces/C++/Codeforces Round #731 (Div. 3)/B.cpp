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
    string s;
    cin >> s;

    int index = s.find_first_of("a");

    if (index == -1) {
        cout << "NO";
        return;
    }

    char current = 'b';
    int r = index - 1, l = index + 1;

    while (r >= 0 || l < s.length()) {
        if (s[r] == current) {
            current++;
            r--;
        } else if (s[l] == current) {
            current++;
            l++;
        } else {
            cout << "NO";
            return;
        }
    }

    cout << "YES";
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