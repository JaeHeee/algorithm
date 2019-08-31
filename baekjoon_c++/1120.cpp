#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	string A;
	string B;
	int diff = 0;
	int min = 50;

	cin >> A >> B;

	for (int i = 0; i <= B.length()-A.length(); i++)
	{
		int k = 0;
		for (int j = i; j < i + A.length(); j++)
		{
			if (A[k] != B[j])
			{
				diff += 1;
			}
			k++;
		}
		if (min > diff)
		{
			min = diff;
		}
		diff = 0;
	}

	cout << min << endl;

	return 0;
}