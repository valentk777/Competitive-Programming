/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/785/problem/A
/* Title  : A. Anton and Polyhedrons
/* Notes  : tag-codeforces, tag-problem-A, tag-div-2
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

int suma = 0, n;
string zodis;

int main()
{
	cin >> n;
	fori(n)
	{
		cin >> zodis;
		if (zodis == "Tetrahedron")
			suma += 4;
		else if (zodis == "Cube")
			suma += 6;
		else if (zodis == "Octahedron")
			suma += 8;
		else if (zodis == "Dodecahedron")
			suma += 12;
		else if (zodis == "Icosahedron")
			suma += 20;
	}
	cout << suma;

	return 0;
}