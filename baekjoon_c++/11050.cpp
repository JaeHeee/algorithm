//binomial coefficient

#include <iostream>
using namespace std;

int main(void) {
	int N;
	int K;
	int binomial[11][10]{ {1,1,1,1,1,1,1,1,1,1},{1,}};
	cin >> N >> K;

	for (int i = 1; i < 11; i++)
	{
		for (int j = 1; j < 10; j++)
		{
			binomial[i][j] = binomial[i][j-1] + binomial[i-1][j-1];
		}
	}

	cout << binomial[K][N - 1] << endl;
	return 0;
}