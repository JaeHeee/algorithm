#include <iostream>

using namespace std;

long long int dp[101][11];

long long int sum_count(int N) {
	for (int i = 0; i < 10; i++)
	{
		dp[N][10] += dp[N][i];
	}

	return dp[N][10];
}

long long int step(int N) {
	if (sum_count(N) != 0)
	{
		return dp[N][10];
	}

	for (int i = 0; i < 10; i++)
	{
		if (i == 0) {
			dp[N][i] = dp[N - 1][i+1]%1000000000;
		}
		else if (i==9)
		{
			dp[N][i] = dp[N - 1][i-1] % 1000000000;
		}
		else {
			dp[N][i] = (dp[N - 1][i - 1] + dp[N - 1][i + 1]) % 1000000000;
		}
	}
	sum_count(N);
	return 0;
}

int main(void) {
	
	int N;

	for (int i = 1; i < 10; i++)
	{
		dp[1][i] = 1;
	}

	cin >> N;

	for (int i = 1; i <= N; i++)
	{
		step(i);
	}

	cout << dp[N][10] %1000000000;

	return 0;
}
