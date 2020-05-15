/*
	강한 결합 요소(Strongly Connected Componet) - 강하게 결합된 정점 집합
	SCC algorithm
		같은 SCC에 속하는 두 정점은 서로 도달이 가능
		사이클이 발생하는 경우 무조건 SCC에 해당한다.
		그래서 방향 그래프일 때만 의미가 있다.
		무향 그래프라면 그 그래프 전체는 무조건 SCC이기 때문이다.

	Tarjan's Algoritm
		모든 정점에 대해서 DFS를 수행하여 SCC를 찾는 알고리즘

	O(V + E)		
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
vector<vector<int>> SCC;
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
		else if(!finished[y])
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
	int n = 11;
	v[1].push_back(2);
	v[2].push_back(3);
	v[3].push_back(1);
	v[4].push_back(2);
	v[4].push_back(5);
	v[5].push_back(7);
	v[6].push_back(5);
	v[7].push_back(6);
	v[8].push_back(5);
	v[8].push_back(9);
	v[9].push_back(10);
	v[10].push_back(11);
	v[11].push_back(8);
	v[11].push_back(3);

	for (int i = 1; i <= n; i++)
	{
		if (d[i] == 0)
			dfs(i);
	}

	cout << "SCC의 개수 : " << SCC.size() << endl;
	for (int i = 0; i < SCC.size(); i++)
	{
		cout << i + 1 << " : ";
		for (int j = 0; j < SCC[i].size(); j++)
		{
			cout << SCC[i][j] << " ";
		}
		cout << endl;
	}

	return 0;

}