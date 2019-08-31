#include <iostream>
#include <algorithm>

using namespace std;

int scales[1001];

int main(void)
{
	int N;
	int min;
	int sum = 0;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> scales[i];
		sum += scales[i];
	}
	min = sum;
	cout << sum << endl;
	sort(scales, scales+N);
	for (int i = 1; i <= sum+1; i++)
	{
		int check = i;
		cout << " 1 " << check << endl;
		while (1)
		{
			int j = 0;
			if (scales[j] <= check)
			{
				check -= scales[j];
			}
			j++;
			if (check == 0)
			{
				cout << "break1" << endl;
				break;
			}
		}
		cout << " 2 "<< check << endl;
		if (check != 0)
		{
			min = i;
			break;
		}
	}
	cout << min << endl;

	return 0;
}