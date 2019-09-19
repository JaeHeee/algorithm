/*
	11376번 열혈강호 3
*/

#include <iostream>
#include <vector>
#define MAX 1001

using namespace std;

vector<int> v[MAX];
int select[MAX];
bool checked[MAX];

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
	int N, M;
	cin >> N >> M;

	for (int i = 1; i <= N; i++)
	{
		int work;
		cin >> work;
		for (int j = 0; j < work; j++)
		{
			int a;
			cin >> a;
			v[i].push_back(a);
		}
	}

	int count = 0;
	for (int j = 0; j < 2; j++)
	{
		for (int i = 1; i <= N; i++)
		{
			fill(checked, checked + MAX, false);
			if (dfs(i))
				count++;
		}
	}
	
	cout << count << endl;
	
	return 0;
}
