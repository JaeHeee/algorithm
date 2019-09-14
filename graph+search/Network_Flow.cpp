/*
	네트워크 플로우(Network Flow)
		특정한 지점에서 다른 지점으로 데이터가 얼마나 많이 흐르고 있는가를 측정하는 알고리즘
	최대 유량(Max Flow)문제
		각 간선에 정해진 용량이 있을 때 A에서 B로 최대로 보낼 수 있는 유량의 크기를 구하는 문제
		BFS를 이용하는 것이 일반적. 에드몬드 카프(Edmonds-Karp) 알고리즘.
		음의 유량 - 남아있는 모든 가능한 경로를 더 찾아내기 위해
*/

#include <iostream>
#include <vector>
#include <queue>

#define MAX 100
#define INF 1000000000

using namespace std;

int n = 6, result=0;
int capacity[MAX][MAX], flow[MAX][MAX], check[MAX];
vector<int> v[MAX];

void maxFlow(int start, int end) {
	while (1) {
		fill(check, check + MAX, -1);
		queue<int> q;
		q.push(start);
		while (!q.empty()) {
			int x = q.front();
			q.pop();
			for (int i = 0; i < v[x].size(); i++) {
				int y = v[x][i];
				if (capacity[x][y] - flow[x][y] > 0 && check[y] == -1) {
					q.push(y);
					check[y] = x;
					if (y == end)
						break;
				}
			}
		}
		if (check[end] == -1)
			break;
		int f = INF;
		for (int i = end; i != start; i = check[i])
		{
			f = min(f, capacity[check[i]][i] - flow[check[i]][i]);
		}

		for (int i = end; i != start; i = check[i])
		{
			flow[check[i]][i] += f;
			flow[i][check[i]] -= f;
		}

		result += f;
	}
}

int main(void) {

	v[1].push_back(2);
	v[2].push_back(1);
	capacity[1][2] = 12;

	v[1].push_back(4);
	v[4].push_back(1);
	capacity[1][4] = 11;

	v[2].push_back(3);
	v[3].push_back(2);
	capacity[2][3] = 6;

	v[2].push_back(4);
	v[4].push_back(2);
	capacity[2][4] = 3;

	v[2].push_back(5);
	v[5].push_back(2);
	capacity[2][5] = 5;

	v[2].push_back(6);
	v[6].push_back(2);
	capacity[2][6] = 9;

	v[3].push_back(6);
	v[6].push_back(3);
	capacity[3][6] = 8;

	v[4].push_back(5);
	v[5].push_back(4);
	capacity[4][5] = 9;

	v[5].push_back(3);
	v[3].push_back(5);
	capacity[5][3] = 3;

	v[5].push_back(6);
	v[6].push_back(5);
	capacity[5][6] = 4;

	maxFlow(1, 6);
	cout << result << endl;

	return 0;
}