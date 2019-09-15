/*
	1516번 게임 개발
*/

#include <iostream>
#include <vector>
#include <queue>
#define MAX 501

using namespace std;

int n, inDegree[MAX], time[MAX], result[MAX];
vector<int> v[MAX];

void topologySort() {
	queue<int> q;

	for (int i = 1; i <= n; i++)
	{
		if (inDegree[i] == 0) {
			result[i] = time[i];
			q.push(i);
		}
	}

	for (int i = 1; i <= n; i++)
	{
		int x = q.front();
		q.pop();
		for (int j = 0; j < v[x].size(); j++)
		{
			int y = v[x][j];
			result[y] = max(result[y], result[x] + time[y]);
			if (--inDegree[y] == 0) {
				q.push(y);
			}
		}
	}

	for (int i = 1; i <= n; i++)
	{
		cout << result[i] << endl;
	}
}

int main(void) {
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> time[i];
		while (1)
		{
			int x;
			cin >> x;
			if (x == -1)
				break;
			inDegree[i]++;
			v[x].push_back(i);
		}
	}
	topologySort();

	return 0;
}