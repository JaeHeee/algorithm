/*
    2150번 Strongly Connected Component
*/

#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#define MAX 10001

using namespace std;

int id, d[MAX];
bool finished[MAX];
vector<int> v[MAX];
vector< vector<int> > SCC;
stack<int> s;

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
			finished[t] = true;
			if (t == x)
				break;
		}
		SCC.push_back(scc);
	}

	return parent;
}

int main(void) {
	int n, e;
	cin >> n >> e;

	for (int i = 0; i < e; i++)
	{
		int a, b;
		cin >> a >> b;
		v[a].push_back(b);
	}

	for (int i = 1; i <= n; i++)
	{
		if (d[i] == 0)
			dfs(i);
	}

	cout << SCC.size() << endl;

	for (int i = 0; i < SCC.size(); i++)
	{
		sort(SCC[i].begin(), SCC[i].end());
	}
	sort(SCC.begin(), SCC.end());
	
	for (int i = 0; i < SCC.size(); i++)
	{
		for (int j = 0; j < SCC[i].size(); j++)
		{
			cout << SCC[i][j] << " ";
		}
		cout << -1;
		cout << endl;
	}


	return 0;

}