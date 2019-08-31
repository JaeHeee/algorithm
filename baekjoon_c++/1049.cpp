#include <iostream>

using namespace std;

int N, M;
int price[50][2];
int money = 0;
int p_min, s_min;

int min(int arr[][2]);
int package_min(int arr[][2]);

int main(void)
{
	cin >> N >> M;

	for (int i = 0; i < M; i++)
	{
		cin >> price[i][0] >> price[i][1];
	}

	p_min = package_min(price);
	s_min = min(price);

	if (p_min == 0 || s_min == 0)
	{
		cout << 0 << endl;
	}
	else if (p_min <= s_min)
	{
		if (N%6 == 0)
		{
			cout << p_min * (N/6) << endl;
		}
		else
		{
			cout << p_min * ((N/6) + 1) << endl;
		}
	}
	else if (p_min > s_min)
	{
		int check = p_min / s_min;
		if (check >= 6)
		{
			cout << s_min * N << endl;
		}
		else
		{
			int r = N % 6;
			if (r == 0)
			{
				cout << p_min * (N / 6) << endl;
			}
			else if (r>check)
			{
				cout << p_min * (1 + N / 6) << endl;
			}
			else if (r<=check)
			{
				cout << s_min * r + p_min * (N / 6) << endl;
			}
		}
	}


	return 0;
}

int min(int arr[][2])
{
	int min = 1000;
	for (int i = 0; i < M; i++)
	{
		if (min > arr[i][1])
		{
			min = arr[i][1];
		}
	}

	return min;
}

int package_min(int arr[][2])
{
	int min = 1000;
	for (int i = 0; i < M; i++)
	{
		if (min > arr[i][0])
		{
			min = arr[i][0];
		}
	}

	return min;
}