/*
	DFS(Depth First Search) - 탐색을 할 때 깊이를 우선으로 하여 탐색을 수행하는 알고리즘
*/

#include <iostream>
#include <vector>

using namespace std;

int number = 7;
int checked[7];
vector<int> v[8];

void dfs(int x) {
	if (checked[x]) return;
	checked[x] = true;
	cout << x << ' ';
	for (int i = 0; i < v[x].size(); i++)
	{
		int y = v[x][i];
		dfs(y);
	}	
}

int main(void) {
	v[1].push_back(2);
	v[2].push_back(1);

	v[1].push_back(3);
	v[3].push_back(1);

	v[2].push_back(3);
	v[3].push_back(2);

	v[2].push_back(4);
	v[4].push_back(2);

	v[2].push_back(5);
	v[5].push_back(2);

	v[3].push_back(6);
	v[6].push_back(3);

	v[3].push_back(7);
	v[7].push_back(3);

	v[4].push_back(5);
	v[5].push_back(4);

	v[6].push_back(7);
	v[7].push_back(6);

	dfs(1);

	return 0;
}