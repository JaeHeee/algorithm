#include <iostream>

using namespace std;

int main(void)
{
	int N, M, K;
	int team = 0;
	cin >> N >> M >> K;

	if (N<2 || M<1)
	{
		cout << team << endl;
	}
	else
	{
		if (N + M >= K && N >= 2 && M >= 1)
		{
			N -= 2;
			M -= 1;
		}
		while (N+M >= K && N>=0 && M>=0)
		{
			team += 1;
			N -= 2;
			M -= 1;
		}
		cout << team << endl;
	}
	return 0;
}