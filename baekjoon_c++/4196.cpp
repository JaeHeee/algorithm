/*
	4196번 도미노
*/

#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#define MAX 100001

using namespace std;

int id, d[MAX];
bool finished[MAX];
vector<int> v[MAX];
vector< vector<int> > SCC;
stack<int> s;
int group[MAX];
bool indegree[MAX];

int dfs(int x) {
	d[x] = ++id;
	s.push(x);

	int parent = d[x];
	for (int i = 0; i < v[x].size(); i++)
	{
		int y = v[x][i];
		if (d[y] == 0)
			parent = min(parent, dfs(y));
		else if (!finished[y])
			parent = min(parent, d[y]);
	}

	if (parent == d[x]) {
		vector<int> scc;
		while (1)
		{
			int t = s.top();
			s.pop();
			scc.push_back(t);
			group[t] = SCC.size() + 1;
			finished[t] = true;
			if (t == x)
				break;
		}
		SCC.push_back(scc);
	}

	return parent;
}

int main(void) {
	int test;
	cin >> test;
	for (int k = 0; k < test; k++)
	{
		SCC.clear();
		fill(d, d + MAX, false);
		fill(finished, finished + MAX, false);
		fill(indegree, indegree + MAX, false);
		int n, e;
		cin >> n >> e;

		for (int j = 1; j <= n; j++)
		{
			v[j].clear();
		}

		for (int i = 0; i < e; i++)
		{
			int a, b;
			cin >> a >> b;
			v[a].push_back(b);
		}

		for (int j = 1; j <= n; j++)
		{
			if (d[j] == 0)
				dfs(j);
		}

		for (int i = 1; i <= n; i++)
		{
			for (int j = 0; j < v[i].size(); j++) {
				int y = v[i][j];
				if (group[i] != group[y])
					indegree[group[y]] = true;
			}
		}

		int result = 0;
		for (int i = 1; i <= SCC.size(); i++)
		{
			if (!indegree[i])
				result++;
		}
		cout << result << endl;
	}

	return 0;

}