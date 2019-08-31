//continuous sum

#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int n;
	cin >> n;
	int * numbers = new int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> numbers[i];
	}
	for (int i = 1; i < n; i++)
	{
		if (numbers[i-1]>0 && numbers[i]+numbers[i-1]>0)
		{
			numbers[i] += numbers[i - 1];
		}
	}
	int result = numbers[0];
	for (int i = 1; i < n; i++)
	{
		result = max(result, numbers[i]);
	}
	cout << result << endl;
	return 0;
}