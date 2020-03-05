#include <iostream>

using namespace std;

int cards[98];

int main(void) {

	int N;
	int M;
	int check;
	int result=0;

	scanf("%d %d", &N, &M);

	for (int i = 0; i < N; i++)
	{
		scanf("%d", &cards[i]);
	}

	if (cards[0] + cards[1] + cards[2] <= M) {
		result = cards[0] + cards[1] + cards[2];
	}
	

	for (int i = 0; i < N-2; i++)
	{
		for (int j = i+1; j < N-1; j++)
		{
			for (int k = j+1; k < N; k++)
			{
				check = cards[i] + cards[j] + cards[k];
				if (check == M)
				{
					result = check;
				}
				else if (check < M && check>result) {
					result = check;
				}
			}
		}
	}

	printf("%d", result);

	return 0;
}
