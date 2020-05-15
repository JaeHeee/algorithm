/*
	Kruskal Algorithm - 가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘
	최소 비용 신장 트리를 만들기 위한 알고리즘
	최소 비용 신장 트리를 만들 때, 사용되는 간선의 개수는 노드 개수 - 1
	모든 간선들을 거리를 기준으로 오름차순 정렬 후, 알고리즘에 맞게 그래프를 연결한다.
	1. 정렬된 순서에 맞게 그래프에 포함시킨다.
	2. 포함시키기 전에는 사이클 확인
	3. 사이클을 형성하는 경우 간선을 포함하지 않는다.
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int getPanrent(int parent[], int x) {
	if (parent[x] == x) return x;
	return parent[x] = getPanrent(parent, parent[x]);
}

void unionParent(int parent[], int a, int b) {
	a = getPanrent(parent, a);
	b = getPanrent(parent, b);
	if (a < b) parent[b] = a;
	else parent[a] = b;
}

int findParent(int parent[], int a, int b) {
	a = getPanrent(parent, a);
	b = getPanrent(parent, b);
	if (a == b) return 1;
	return 0;
}

class Edge {
public:
	int node[2];
	int distance;
	Edge(int a, int b, int distance) {
		this->node[0] = a;
		this->node[1] = b;
		this->distance = distance;
	}
	bool operator <(Edge &edge) {
		return this->distance < edge.distance;
	}
};
int main(void) {
	int m = 11;

	vector<Edge> v;
	v.push_back(Edge(1, 7, 12));
	v.push_back(Edge(1, 4, 28));
	v.push_back(Edge(1, 2, 67));
	v.push_back(Edge(1, 5, 17));
	v.push_back(Edge(2, 4, 24));
	v.push_back(Edge(2, 5, 62));
	v.push_back(Edge(3, 5, 20));
	v.push_back(Edge(3, 6, 37));
	v.push_back(Edge(4, 7, 13));
	v.push_back(Edge(5, 6, 45));
	v.push_back(Edge(5, 7, 73));

	sort(v.begin(), v.end());

	int parent[8];
	for (int i = 1; i <= 7; i++)
	{
		parent[i] = i;
	}

	int sum = 0;
	for (int i = 0; i < v.size(); i++)
	{
		if (!findParent(parent, v[i].node[0], v[i].node[1]))
		{
			sum += v[i].distance;
			unionParent(parent, v[i].node[0], v[i].node[1]);
		}
	}

	cout << sum << endl;

	return 0;
}
