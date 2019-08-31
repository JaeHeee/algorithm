#include <iostream>
#include <math.h>

using namespace std;

int location[21];

int main(void) {
	int N, M, J;
	int distance = 0;
	cin >> N >> M;
	cin >> J;

	for (int i = 1; i <= J; i++)
	{
		cin >> location[i];
	}
	
	if (M == 1)
	{
		for (int i = 1; i < J; i++)
		{
			distance += abs(location[i + 1] - location[i]);
		}
	}
	else
	{
		int left = 1;
		int right = M;
		for (int i = 1; i <= J; i++)
		{
			if (left <= location[i] && location[i] <= right)
			{
				distance += 0;
			}
			else if (location[i] > right)
			{
				distance += (location[i] - right);
				left += (location[i] - right);
				right += (location[i] - right);
			}
			else if (location[i] < left)
			{
				distance += (left - location[i]);
				right -= (left - location[i]);
				left -= (left - location[i]);
			}
		}
	}

	cout << distance << endl;

	return 0;
}