#include <iostream>

using namespace std;


int main(void)
{
	int N;
	int M;

	cin >> N >> M;
	
	if (N == 1)
	{
		cout << 1;
	}
	else if (N == 2)
	{
		if (M > 6)
		{
			cout << 4;
		}
		else
		{
			cout << (M / 2) + (M % 2);
		}

	}
	else
	{
		if (M>=7)
		{
			cout << M - 7 + 5;
		}
		else if (M <= 4)
		{
			cout << M;
		}
		else
		{
			cout << 4;
		}
	}
	
	return 0;
}