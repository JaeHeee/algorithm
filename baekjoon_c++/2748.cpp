#include <iostream>

using namespace std;

long long int dp[91];

long long int fib(long long int n)
{
	if (dp[n] != 0)
	{
		return dp[n];
	}
	return dp[n] = fib(n-1) + fib(n-2);
}

int main(void) {

	long long int N;
	
	scanf("%lld", &N);
	
	dp[1] = 1;
	dp[2] = 1;
	printf("%lld", fib(N));
	
	return 0;
}
