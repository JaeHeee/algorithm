/*
	Lowest Common Ancestor
	트리 구조에서 특정한 두 노드의 공통된 조상 중에서 가장 가까운 조상
	1. 모든 노드에 대한 깊이를 구한다.
	2. 모든 노드에 대한 2^i번째 부모 노드를 구한다.
	3. 최소 공통 조상을 찾을 두 노드를 설정한다.
	4. 두 노드의 깊이가 동일하도록 거슬러 올라간다.
	5. 최상단 노드부터 내려오는 방식으로 두 노드의 공통 부모를 찾아낸다.
*/

#include <iostream>
#include <vector>
#define MAX 1001
#define LOG 11

using namespace std;

int n, m, parent[MAX][LOG], dep[MAX];
bool checked[MAX];
vector<int> a[MAX];

void dfs(int x, int depth) {
	checked[x] = true;
	dep[x] = depth;
	for (int i = 0; i < a[x].size(); i++)
	{
		int y = a[x][i];
		if (checked[y]) continue;
		parent[y][0] = x;
		dfs(y, depth + 1);
	}
}

void setParent() {
	dfs(0, 0);
	for (int i = 1; i < LOG; i++)
	{
		for (int j = 0; j < n; j++)
		{
			parent[j][i] = parent[parent[j][i - 1]][i - 1];
		}
	}
}

int LCA(int x, int y) {
	if (dep[x] > dep[y]) {
		swap(x, y);
	}

	for (int i = LOG - 1; i>=0 ; i--)
	{
		if (dep[y] - dep[x] >= (1 << i)) {
			y = parent[y][i];
		}
	}

	if (x == y) return x;
	for (int i = LOG - 1; i >= 0; i--)
	{
		if (parent[x][i] != parent[y][i]) {
			x = parent[x][i];
			y = parent[y][i];
		}
	}

	return parent[x][0];
}

int main(void) {
	n = 21;

	a[0].push_back(1);
	a[1].push_back(0);

	a[0].push_back(2);
	a[2].push_back(0);

	a[1].push_back(3);
	a[3].push_back(1);

	a[1].push_back(4);
	a[4].push_back(1);

	a[2].push_back(5);
	a[5].push_back(2);

	a[2].push_back(6);
	a[6].push_back(2);

	a[3].push_back(7);
	a[7].push_back(3);

	a[3].push_back(8);
	a[8].push_back(3);

	a[4].push_back(9);
	a[9].push_back(4);

	a[4].push_back(10);
	a[10].push_back(4);

	a[4].push_back(11);
	a[11].push_back(4);

	a[8].push_back(12);
	a[12].push_back(8);

	a[8].push_back(13);
	a[13].push_back(8);

	a[9].push_back(14);
	a[14].push_back(9);

	a[10].push_back(15);
	a[15].push_back(10);

	a[13].push_back(16);
	a[16].push_back(13);

	a[13].push_back(17);
	a[17].push_back(13);

	a[14].push_back(18);
	a[18].push_back(14);

	a[15].push_back(19);
	a[19].push_back(15);

	a[17].push_back(20);
	a[20].push_back(17);

	setParent();
	cout << "5 & 7 LCA : " << LCA(5, 7) << "\n";
	cout << "15 & 20 LCA : " << LCA(15, 20) << "\n";
	cout << "20 & 15 LCA : " << LCA(20, 15) << "\n";
	cout << "4 & 9 LCA : " << LCA(4, 9) << "\n";
	cout << "16 & 17 LCA : " << LCA(16, 17) << "\n";
	cout << "10 & 9 LCA : " << LCA(10, 9) << "\n";
	cout << "3 & 17 LCA : " << LCA(3, 17) << "\n";

	return 0;
}