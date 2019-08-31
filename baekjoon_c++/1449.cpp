#include <iostream>
#include <algorithm>

using namespace std;

double index[1000];

int main(void) {
	int count = 1;
	int N, L;
	cin >> N >> L;

	for (int i = 0; i < N; i++)
	{
		cin >> index[i];
	}

	if (N == 1)
	{
		cout << count << endl;
	}
	else
	{
		sort(index, index + N);

		double tape_start = index[0] - 0.5;
		double tape_end = tape_start + L;


		for (int i = 1; i < N; i++)
		{
			if (index[i]-0.5 > tape_end)
			{
				tape_start = index[i] - 0.5;
				tape_end = tape_start + L;
				count++;
			}
			else if (index[i] + 0.5 > tape_end && index[i] - 0.5 <= tape_end)
			{
				tape_start = tape_end;
				tape_end = tape_start + L;
				count++;
			}
		}

		cout << count << endl;
	}

	


	return 0;
}