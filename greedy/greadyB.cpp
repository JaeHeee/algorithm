/*
	구글코드잼(Google Code Jam) 2018 Qualification Round
	Trouble Sort
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> odd;
vector<int> even;

int main(void) {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		odd.clear();
		even.clear();
		cout << "CASE #" << i + 1 << ": ";
		int N;
		cin >> N;
		for (int j = 0; j < N; j++)
		{
			int number;
			cin >> number;
			if (j % 2 == 0)
			{
				odd.push_back(number);
			}
			else
			{
				even.push_back(number);
			}
		}
		sort(odd.begin(), odd.end());
		sort(even.begin(), even.end());
		int now = 0;
		bool sorted = true;
		for (int i = 0; i < N; i++)
		{
			if (i % 2 == 0)
			{
				if (odd[i / 2] < now) {
					cout << i - 1 << '\n';
					sorted = false;
					break;
				}
				else {
					now = odd[i / 2];
				}
			}
			else
			{
				if (even[i / 2] < now) {
					cout << i - 1 << '\n';
					sorted = false;
					break;
				}
				else {
					now = even[i / 2];
				}
			}
		}
		if (sorted)
		{
			cout << "OK" << "\n";
		}
	}

	return 0;
}