/*
	세그먼트 트리(Segment Tree)
		데이터의 합을 가장 빠르고 간단하게 구할 수 있는 자료구조
		최상단 노드 = 전체합
		2번 노드 - 0 ~ 5번 인덱스 합
		3번 노드 - 6 ~ 11번 인덱스 합
		원래 데이터의 범위를 반씩 분할하며 그 구간의 합들을 저장하도록 초기 설정
		구간 합 트리의 인덱스는 1부터 시작 - 2를 곱했을 때 왼쪽 자식노들를 가리키므로 효과적
		데이터의 개수가 n개일 때 n보다 큰 가장 가까운 제곱수를 구한 뒤에 그것의 2배까지
		미리 배열의 크기를 만들어놓아야 한다.
		실제로는 데이터의 개수 n에 4를 곱한 크기만큼 미리 구간 합 트리의 공간을 할당
*/

#include <iostream>
#define NUMBER 12

using namespace std;

int a[] = { 1,9,3,8,4,5,5,9,10,3,4,5 };
int tree[4 * NUMBER];

int init(int start, int end, int node) {
	if (start == end) {
		return tree[node] = a[start];
	}
	int mid = (start + end) / 2;
	return tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2+1);
}

int sum(int start, int end, int node, int left, int right) {
	if (left > end || right < start)
		return 0;
	if (left <= start && end <= right)
		return tree[node];
	int mid = (start + end) / 2;
	return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right);
}

void update(int start, int end, int node, int index, int dif) {
	if (index < start || index > end) return;
	tree[node] += dif;
	if (start == end) return;
	int mid = (start + end) / 2;
	update(start, mid, node * 2, index, dif);
	update(mid+1, end, node * 2+1, index, dif);
}

int main(void) {
	init(0, NUMBER - 1, 1);
	cout << "0~11 구간 합: " << sum(0, NUMBER - 1, 1, 0, 11) << endl;
	cout << "3~8 구간 합: " << sum(0, NUMBER - 1, 1, 3, 8) << endl;
	cout << "5의 원소를 -5 만큼 수정" << endl;
	update(0, NUMBER - 1, 1, 5, -5);
	cout << "3~8 구간 합: " << sum(0, NUMBER - 1, 1, 3, 8) << endl;

	return 0;

}