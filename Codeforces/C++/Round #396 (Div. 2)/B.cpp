/*-----------------------------------------------------------*/
/* URL    : https://codeforces.com/contest/766/problem/B
/* Title  : B. Mahmoud and a Triangle
/* Notes  : tag-codeforces, tag-problem-B, tag-div-2
/*-----------------------------------------------------------*/
/*-------- valentk777 --------*/
#include <iostream>	 // std::cout
#include <algorithm> // std::sort
#include <vector>	 // std::vector

using namespace std;

int main()
{
	int n;
	cin >> n;
	long long int input;

	vector<int> V;
	for (int i = 0; i < n; i++)
	{
		cin >> input;
		V.push_back(input);
	}

	sort(V.begin(), V.end());

	for (int k = 1; k <= n; k++)
	{
		for (int i = 1; i <= n - k; i++)
		{
			for (int j = 1; j <= n - k - i; i++)
			{
				if (V[n - k] - V[n - k - i] < V[n - k - i - j])
					return 0 * puts("YES");
			}
		}
	}
	cout << "NO";
	return 0;
}