/*
	구글코드잼(Google Code Jam) 2018 Qualification Round
	Saving The Universe Again
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

vector<int> v;

bool compare(int a, int b) {
	return a > b;
}

int main(void) {
	int T = 0;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		int D, strength = 1, strengthSum = 0, count = 0, countSum = 1;
		string P;
		cin >> D >> P;
		v.clear();
		for (int j = 0; j < P.size(); j++)
		{
			if (P[j] == 'C') {
				count++;
				strength *= 2;
			}
			else {
				countSum += count;
				strengthSum += strength;
				v.push_back(strength);
			}
		}
		bool find = false;
		int k = 0;
		while (countSum--) {
			if (strengthSum <= D) {
				find = true;
				cout << k << '\n';
				break;
			}
			sort(v.begin(), v.end(), compare);
			strengthSum -= v[0] / 2;
			v[0] /= 2;
			k++;
		}
		if (!find) cout << "IMPOSSIBLE" << '\n';
	}

	return 0;
}
