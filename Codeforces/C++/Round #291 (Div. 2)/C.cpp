/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/514/problem/C
/* Title  : Watto and Mechanism
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

ll power[600000];

ll computeHashCode(string& s) {
    ll n = s.length();
    ll hash_val = 0;
    int base = 3;  // should be prime

    forn(i, n) {
        hash_val = (hash_val + (s[i] - 'a' + 1) * power[i]);
    }

    return hash_val;
}

bool findIfExist(ll f, vector<ll> v, ll _right = 0) {
    ll left = 0, right = v.size() - 1;

    while (left <= right) {
        ll mid = (left + right) / 2;

        // cout << "mid: " << mid << endl;
        // cout << "left: " << left<< endl;
        // cout << "right: " << right<< endl;
        // cout<< endl;

        if (v[mid] < f) {
            left = mid + 1;
        } else if (v[mid] > f) {
            right = mid - 1;
        } else {
            return true;
        }
    }

    return false;
}

void solve_with_hash_with_error() {
    // fill global variable with values. this is for faster hasing
    power[0] = 1;
    for (ll i = 1; i < 600000; i++)
        power[i] = power[i - 1] * 3;

    ll n, m;
    cin >> n >> m;

    set<ll> a;

    string current;

    while (n--) {
        cin >> current;
        a.insert(computeHashCode(current));
    }

    // this needs to have access via index
    vector<ll> v(a.begin(), a.end());

    while (m--) {
        cin >> current;

        ll len = current.length();

        if (len == 0) {
            cout << "NO" << endl;
            continue;
        }

        bool found = false;

        ll original_hash = computeHashCode(current);
        ll new_hash = 0;

        forn(li, len) {
            for (auto letter : {'a', 'b', 'c'}) {
                if (current[li] == letter) {
                    continue;
                }

                new_hash = original_hash - (current[li] - 'a' + 1) * power[li] + (letter - 'a' + 1) * power[li];

                if (findIfExist(new_hash, v)) {
                    found = true;
                    break;
                }
            }

            if (found) {
                break;
            }
        }

        if (found) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}

void solve_to_slow() {
    ll n, m;
    cin >> n >> m;

    set<string> a;

    string current;

    forn(i, n) {
        cin >> current;
        a.insert(current);
    }

    forn(i, m) {
        cin >> current;
        ll current_length = current.length();

        bool found = false;

        for (auto ita : a) {
            string current_a = ita;

            if (current_a.length() == current_length) {
                if (current == current_a) {
                    continue;
                }

                ll left = 0, right = current_length;

                while (left <= right) {
                    ll mid = (left + right) / 2;

                    if (mid - left != 0 && current.substr(left, mid - left) == current_a.substr(left, mid - left)) {
                        left = mid;
                    } else if (right - mid != 0 && current.substr(mid, right - mid) == current_a.substr(mid, right - mid)) {
                        right = mid;
                    } else if (right - left == 1) {
                        found = true;
                        break;
                    } else {
                        break;
                    }
                }
            }
        }

        if (found) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
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