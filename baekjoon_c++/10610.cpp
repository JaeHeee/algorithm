#include <iostream>
#include <string>

using namespace std;

int numbers[10];

int main(void)
{
	int temp = 0;
	string N;
	cin >> N;
	for (int i = 0; i < N.size(); i++)
	{
		numbers[N[i]-'0']++;
		temp += (N[i] - '0');
	}
	if (temp % 3==0 && numbers[0] != 0)
	{
		for (int i = 9; i >= 0; i--)
		{
			for (int j = 0; j < numbers[i]; j++)
			{
				cout << i;
			}
		}
	}
	else
	{
		cout << -1;
	}
	
	
	return 0;
}