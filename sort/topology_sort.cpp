/*
	위상 정렬(Topology Sort)
	순서가 정해져있는 작업을 차례로 수행해야 할 때 그 순서를 결정해주기 위해 사용하는 알고리즘
	여러 개의 답이 존재할 수 있다.
	DAG(Directed Acyclic Graph)에만 적용 가능 cycle이 있으면 시작점이 없기 때문에
	위상 정렬은 두 가지 해결책 제시
	1. 현재 그래프는 위상 정렬이 가능한지
	2. 위상 정렬이 가능하다면 그 결과는 무엇인지

	큐를 이용한 방식
	1. 진입차수(특정한 노드로 들어오는 다른 노드의 개수)가 0인 정점을 큐에 삽입
	2. 큐에서 원소를 꺼내 연결된 모든 간선을 제거
	3. 간선 제거 이후에 진입차수가 0이 된 정점을 큐에 삽입.
	4. 큐가 빌 때까지 2~3번 과정 반복. 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재하는 것이고, 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과
	O(V+E) 정점의 개수 + 간선의 개수

*/

#include <iostream>
#include <vector>
#include <queue>
#define MAX 10

using namespace std;

int n, inDegree[MAX];
vector<int> v[MAX];

void topologySort() {
	int result[MAX];
	queue<int> q;
	for (int i = 1; i <= n; i++)
	{
		if (inDegree[i] == 0)
			q.push(i);
	}

	for (int i = 1; i <= n; i++)
	{
		if (q.empty()) {
			cout << "cycle!!!" << endl;
			return;
		}
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
		cout << result[i] << endl;
	}
}

int main(void) {
	n = 7;
	v[1].push_back(2);
	inDegree[2]++;
	v[1].push_back(5);
	inDegree[5]++;
	v[2].push_back(3);
	inDegree[3]++;
	v[3].push_back(4);
	inDegree[4]++;
	v[4].push_back(6);
	inDegree[6]++;
	v[6].push_back(7);
	inDegree[7]++;
	topologySort();

	return 0;
}
