#include <iostream>

using namespace std;

int number[11] = { 0, };

int main(void)
{
	int N;	

	cin >> N; 
	for (int i = 1; i <= N; i++)
	{
		int value;
		cin >> value;
		int count = 0;
		for (int j = 1; j <= N; j++)
		{
			if (count == value && number[j] == 0)
			{
				number[j] = i;
				break;
			}
			if (number[j] == 0)
			{
				count++;
			}
		}
	}
	
	for (int i = 1; i <= N; i++)
	{
		cout << number[i] << " ";
	}

	return 0;
}