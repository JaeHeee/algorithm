/*
	이분 매칭(Bipartite Matching)
		네트워크 플로우 알고리즘과 연계되는 개념
		A 집단이 B 집단을 선택하는 방법에 대한 알고리즘
*/

#include <iostream>
#include <vector>
#define MAX 101

using namespace std;

vector<int> v[MAX];
int select[MAX];
bool checked[MAX];

int n = 3, m;

bool dfs(int x) {
	for (int i = 0; i < v[x].size(); i++)
	{
		int t = v[x][i];
		if (checked[t])
			continue;
		checked[t] = true;
		if (select[t] == 0 || dfs(select[t])) {
			select[t] = x;
			return true;
		}
	}
	return false;
}

int main(void) {
	v[1].push_back(1);
	v[1].push_back(2);
	v[1].push_back(3);
	v[2].push_back(1);
	v[3].push_back(2);
	
	int count = 0;
	for (int i = 1; i <= n; i++)
	{
		fill(checked, checked + MAX, false);
		if (dfs(i))
			count++;
	}
	cout << count << " 개" << endl;
	for (int i = 1; i < MAX; i++) {
		if (select[i] != 0) {
			cout << select[i] << " -> " << i << endl;
		}
	}
	return 0;
}