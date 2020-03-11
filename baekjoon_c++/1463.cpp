#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int dp[1000001];
double cube;

int counter(int N) {
	int check = N;
	if (dp[check] != 0 || N==1)
	{
		return dp[check];
	}
	cube = pow(check, 1.0 / 3.0);
	if (fmod(cube, 3) == 0.0 || check % 3 == 0)
	{
		check /= 3;
	}
	else if (sqrt(check) == 0 || check % 2 == 0)
	{
		check /= 2;
	}
	else {
		check -= 1;
		return dp[N] = counter(check) + 1;
	}
	
	return dp[N] = min(counter(N-1),counter(check))+1;
}

int main(void) {

	int N;

	scanf("%d", &N);

	dp[1] = 0;
	dp[2] = 1;
	dp[3] = 1;

	printf("%d", counter(N));

	return 0;
}
