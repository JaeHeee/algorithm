// coin 1

#include<iostream>
using namespace std;

int main(void) {

	int	N , K;
	cin >> N;
	cin >> K;
	int *coin = new int[N];
	for (int i = 0; i < N; i++)
	{
		cin >> coin[i];
	}
	int *dp = new int[K+1];
	dp[0] = 1;
	for (int i = 1; i < K+1; i++)
	{
		if (i%coin[0]==0)
		{
			dp[i] = 1;
		}
		else
		{
			dp[i] = 0;
		}
	}

	for (int i = 1; i < N; i++)
	{
		for (int j = 1; j < K+1; j++)
		{
			if (coin[i] <= j)
			{
				dp[j] += dp[j - coin[i]];
			}
		}
	}
	
	cout << dp[K] << endl;

	delete[] coin;
	delete[] dp;
	return 0;
}
