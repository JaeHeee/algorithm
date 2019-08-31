//Padovan Sequence

#include<iostream>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	int * numbers = new int[T];
	long long dp[100];
	dp[0] = 1, dp[1] = 1, dp[2] = 1, dp[3] = 2, dp[4] = 2;
	for (int i = 0; i < T; i++)
	{
		cin >> numbers[i];
		if (numbers[i]<=5)
		{
			cout << dp[numbers[i] - 1] << endl;
		}
		else
		{
			for (int j = 5; j < numbers[i]; j++)
			{
				dp[j] = dp[j - 1] + dp[j - 5];
			}
			cout << dp[numbers[i]-1] << endl;
		}
	}
	delete[] numbers;
	return 0;
}