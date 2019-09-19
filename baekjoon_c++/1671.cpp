/*
	1671번 상어의 저녁식사
*/

#include <iostream>
#include <vector>
#define MAX 50

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
	int N;
	int stat[MAX][3];
	cin >> N;
	
	for (int i = 1; i <= N ; i++)
	{
		cin >> stat[i][0] >> stat[i][1] >> stat[i][2];
	}

	for (int i = 1; i < N; i++)
	{
		for (int j = i+1; j <= N; j++)
		{
			if (stat[i][0] >= stat[j][0] && stat[i][1] >= stat[j][1] && stat[i][2] >= stat[j][2]) {
				v[i].push_back(j);
			}
			else if (stat[i][0] == stat[j][0] && stat[i][1] == stat[j][1] && stat[i][2] == stat[j][2]) {
				v[i].push_back(j);
			}
			else if (stat[i][0] <= stat[j][0] && stat[i][1] <= stat[j][1] && stat[i][2] <= stat[j][2]) {
				v[j].push_back(i);
			}
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
	
	cout << N - count << endl;
	
	return 0;
}
