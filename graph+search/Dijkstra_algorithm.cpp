/*
	Dijkstra Algorithm - 최단 경로 탐색 알고리즘
	특정한 하나의 정점에서 다른 모든 정점으로 가는 최단경로를 알려준다.
	하나의 최단 거리를 구할 때 그 이전 까지의 최단 거리 정보를 그대로 사용한다.
	1.출발 노드를 설정
	2.출발 노드를 기준으로 각 노드의 최소 비용을 저장
	3.방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택
	4.해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 갱신
	5.3번4번 반복
*/

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int number = 6;
int INF = 1000000000;

vector<pair<int, int>> v[7];
int minimum[7];

void dijkstra(int start) {
	minimum[start] = 0;
	priority_queue<pair<int, int>> pq;
	pq.push(make_pair(start, 0));
	while (!pq.empty())
	{
		int current = pq.top().first;
		//짧은 것이 먼저 오도록 음수화
		int distance = -pq.top().second;
		pq.pop();
		if (minimum[current] < distance) continue;
		for (int i = 0; i < v[current].size(); i++)
		{
			int next = v[current][i].first;
			int nextDistance = distance + v[current][i].second;
			if (nextDistance < minimum[next]) {
				minimum[next] = nextDistance;
				pq.push(make_pair(next, -nextDistance));
			}
		}
	}
}

int main(void) {
	for (int i = 1; i <= number; i++)
	{
		minimum[i] = INF;
	}

	v[1].push_back(make_pair(2, 2));
	v[1].push_back(make_pair(3, 5));
	v[1].push_back(make_pair(4, 1));

	v[2].push_back(make_pair(1, 2));
	v[2].push_back(make_pair(3, 3));
	v[2].push_back(make_pair(4, 2));

	v[3].push_back(make_pair(1, 5));
	v[3].push_back(make_pair(2, 3));
	v[3].push_back(make_pair(4, 3));
	v[3].push_back(make_pair(5, 1));
	v[3].push_back(make_pair(6, 5));

	v[4].push_back(make_pair(1, 1));
	v[4].push_back(make_pair(2, 2));
	v[4].push_back(make_pair(3, 3));
	v[4].push_back(make_pair(5, 1));

	v[5].push_back(make_pair(3, 1));
	v[5].push_back(make_pair(4, 1));
	v[5].push_back(make_pair(6, 2));

	v[6].push_back(make_pair(3, 5));
	v[6].push_back(make_pair(5, 2));
	
	dijkstra(1);

	for (int i = 1; i <= number; i++)
	{
		cout << minimum[i] << " ";
		cout << endl;
	}

	return 0;
}
