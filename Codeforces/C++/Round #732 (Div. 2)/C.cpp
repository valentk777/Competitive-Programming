/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/1546/problem/C
/* Title  : AquaMoon and Strange Sort
/* Notes  : tag-codeforces, tag-problem-C, tag-div-2, tag-not-pass
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
#define max_tuple(x, n) *max_element(x, x + n, [](const auto& lhs, const auto& rhs) { return lhs.first < rhs.first; })
#define min_tuple(x, n) *min_element(x, x + n, [](const auto& lhs, const auto& rhs) { return lhs.first < rhs.first; })
#define max_tuple_y(x, y, n) *max_element(x + y, x + n, [](const auto& lhs, const auto& rhs) { return lhs.first < rhs.first; })
#define min_tuple_y(x, y, n) *min_element(x + y, x + n, [](const auto& lhs, const auto& rhs) { return lhs.first < rhs.first; })

#define test() ll t; cin >> t; while (t--)
#define dbg(x) cout<<#x<<" = "<<x<<endl;

/*----------------------------*/

const int max_n=1e5+5;

void IO() {
    #ifndef ONLINE_JUDGE
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);
    #endif
    fast_cin();
}

void solve2() {
    ll n;
    cin >> n;
    
    vector<int> a(n + 1), ind(n + 1);

    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        ind[i] = i;
    }

    sort(ind.begin() + 1, ind.end(), [&a](const int aa, const int bb) -> bool {
        if (a[aa] == a[bb])
            return aa < bb;
        else
            return a[aa] < a[bb];
    });

    bool flag = true;
    vector<int> vis(max_n);

    for (int i = 1; i <= n; i++) {
        vis[a[ind[i]]] += abs(ind[i] - i);
    }

    for (int i = 0; i < max_n && flag; i++) {
        flag = (vis[i] % 2 == 0);
    }

    cout << (!flag ? "NO" : "YES");
}

void solve() {
    ll n;
    cin >> n;

    pair<ll, ll> a[n];
    forn(i, n) {
        cin >> a[i].first;
        a[i].second = i;
    }

    sort(a, a + n);

    forn(i, n) {
        if (a[i].second % 2 != i % 2) {
            cout << "NO";
            return;
        }
    }

    cout << "YES";
}

void solution_to_slow_improved() {
    ll n;
    cin >> n;

    pair<ll, ll> a[n];

    forn(i, n) {
        cin >> a[i].first;
        a[i].second = i;
    }

    ll current_min_ind = 0;

    while (true) {
        auto current_min = min_tuple(a, n);

        if ((current_min.second - current_min_ind) % 2 == 0) {
            current_min_ind++;
            a[current_min.second].first = 1000000;
        } else if (current_min.first == 1000000) {
            cout << "YES";
            return;
        } else if (current_min.second + 1 < n) {
            auto new_min = min_tuple_y(a, current_min.second + 1, n);
            if (new_min.first == current_min.first) {
                if ((new_min.second - current_min_ind) % 2 == 0) {
                    current_min_ind++;
                    a[new_min.second].first = 1000000;
                }
            } else {
                break;
            }
        } else {
            break;
        }
    }

    cout << "NO";
}

void solution_to_slow() {
    ll n;
    cin >> n;

    ll a[n];

    forn(i, n) cin >> a[i];

    ll current_min_ind = 0;

    while (true) {
        ll* current_min = min_element(a, a + n);
        ll pmin = distance(a, current_min);

        if ((pmin - current_min_ind) % 2 == 0) {
            current_min_ind++;
            a[pmin] = 1000000;
        } else if (*current_min == 1000000) {
            cout << "YES";
            return;
        } else if (pmin + 1 < n) {
            ll* new_min = min_element(a + pmin + 1, a + n);

            if (*new_min == *current_min) {
                ll pp_min = distance(a, new_min);

                if ((pp_min - current_min_ind) % 2 == 0) {
                    current_min_ind++;
                    a[pp_min] = 1000000;
                }
            } else {
                break;
            }
        } else {
            break;
        }
    }

    cout << "NO";
}

int main() {
    IO();

    test() {
#ifdef ONLINE_JUDGE
        solve2();
#else
        time__("Run duration: ") solve2();
#endif

        cout << endl;
    }

    return 0;
}