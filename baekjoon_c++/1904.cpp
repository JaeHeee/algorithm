	#include <iostream>

	using namespace std;

	int dp[1000001];

	int tile(int N) {
		if (N == 1) return dp[1] = 1;
		if (N == 2) return dp[2] = 2;
		if (dp[N] != 0)
		{
			return dp[N];
		}
		return dp[N] = (tile(N - 1) + tile(N - 2))%15746;
	}

	int main(void) {

		int N;
		scanf("%d", &N);
		printf("%d", tile(N));

		return 0;

	}
