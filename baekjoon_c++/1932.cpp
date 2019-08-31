//integer triangle

#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

int main(void)
{
	//Å©±â
	int N;
	cin >> N;
	//»ï°¢Çü
	int **triangle = new int*[N];
	for (int i = 0; i < N; i++)
	{
		triangle[i] = new int[i+1];
	}
	
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < i+1; j++)
		{
			cin >> triangle[i][j];
		}
	}
	
	if (N == 1)
	{
		cout << triangle[0][0] << endl;
	}
	else if (N>1)
	{
		//dp
		int **dp = new int*[N];
		for (int i = 0; i < N; i++)
		{
			dp[i] = new int[i+1];
		}
		dp[0][0] = triangle[0][0];
		
		for (int i = 1; i < N; i++)
		{
			for (int j = 0; j < i+1; j++)
			{
				if (j==0)
				{
					dp[i][j] = dp[i - 1][j] + triangle[i][j];
				}
				else if (j==i)
				{
					dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];
				}
				else
				{
					dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j];
				}			
			}
		}

		//max
		int result = 0;
		for (int i = 0; i < N; i++)
		{
			result = max(result, dp[N - 1][i]);
		}

		cout << result << endl;

		//delete dp
		for (int i = 0; i < N; i++)
		{
			delete[] dp[i];
		}
		delete[] dp;
	}
	//delete triangle
	for (int i = 0; i < N; i++)
	{
		delete[] triangle[i];
	}
	delete[] triangle;
	return 0;
}