/*
	2252번 줄 세우기
*/

#include <iostream>
#include <vector>
#include <queue>
#define MAX 32001

using namespace std;

int n, inDegree[MAX], result[MAX];
vector<int> v[MAX];

void topologySort() {
	queue<int> q;

	for (int i = 1; i <= n; i++)
	{
		if (inDegree[i] == 0) {
			q.push(i);
		}
	}

	for (int i = 1; i <= n; i++)
	{
		int x = q.front();
		q.pop();
		result[i] = x;
		for (int j = 0; j < v[x].size(); j++)
		{
			int y = v[x][j];
			if (--inDegree[y] == 0) {
				q.push(y);
			}
		}
	}

	for (int i = 1; i <= n; i++)
	{
		cout << result[i] << " ";
	}
}

int main(void) {
	int m;
	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		int x, y;
		cin >> x >> y;
		v[x].push_back(y);
		inDegree[y]++;
	}
	topologySort();

	return 0;
}