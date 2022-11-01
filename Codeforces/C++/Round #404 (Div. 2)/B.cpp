/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/785/problem/B
/* Title  : B. Anton and Classes
/* Notes  : tag-codeforces, tag-problem-B, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>

using namespace std;
typedef long long ll;

#define fori(n) for (int i = 0; i < n; i++)
#define fork(n) for (int k = 0; k < n; k++)
#define forj(n) for (int j = 0; j < n; j++)
#define fori1(n) for (int i = 1; i <= n; i++)
#define fork1(n) for (int k = 1; k <= n; k++)
#define forj1(n) for (int j = 1; j <= n; j++)
#define maximalus 1000000002

int n, m;
ll didz[] = {0, 0}, mazas[] = {maximalus, maximalus};

ll did(ll a, ll b);
ll maz(ll a, ll b);

int main()
{
	cin >> n;
	fori(n)
	{
		int a, b;
		cin >> a >> b;
		mazas[0] = maz(mazas[0], b);
		didz[0] = did(didz[0], a);
	}
	cin >> m;
	fori(m)
	{
		int a, b;
		cin >> a >> b;
		mazas[1] = maz(mazas[1], b);
		didz[1] = did(didz[1], a);
	}

	cout << did(0, did(didz[1] - mazas[0], didz[0] - mazas[1]));
	return 0;
}

ll did(ll a, ll b)
{
	if (a > b)
		return a;
	else
		return b;
}

ll maz(ll a, ll b)
{
	if (a < b)
		return a;
	else
		return b;
}