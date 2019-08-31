#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int, int>> score;

int main(void)
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int N;
		int emp = 0;
		int min = 100001;
		cin >> N;
		score.clear();

		for (int j = 0; j < N; j++)
		{
			int re, in;
			cin >> re >> in;
			score.push_back(make_pair(re, in));
		}

		sort(score.begin(), score.end());
		
		for (int k = 0; k < N; k++)
		{
			if (min > score[k].second)
			{
				min = score[k].second;
				emp++;
			}
		}

		cout << emp << endl;
	}
	
	return 0;
}