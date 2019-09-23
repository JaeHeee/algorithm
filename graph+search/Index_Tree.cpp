/*
	인덱스 트리(Index Tree)
		2진 인덱스 구조를 활용하여 '구간 합' 문제를 효과적으로 해결해 줄 수 있는 자료구조
		마지막 비트 = 내가 저장하고 있는 값들의 개수
*/

#include <iostream>
#define NUMBER 6

using namespace std;

int tree[NUMBER];

void update(int i, int diff){
	while (i <= NUMBER) {
		tree[i] += diff;
		i += (i & -i);
	}
}

int sum(int i) {
	int res = 0;
	while (i > 0) {
		res += tree[i];
		i -= (i &-i);
	}
	return res;
}

int getSection(int start, int end) {
	return sum(end) - sum(start - 1);
}

int main(void) {
	update(1, 1);
	update(2, 2);
	update(3, 3);
	update(4, 4);
	update(5, 5);

	cout << "2 ~ 5 : " << getSection(2, 5) << endl;
	cout << "3 -> -2" << endl;
	update(3, -2);
	cout << "2 ~ 5 : " << getSection(2, 5) << endl;
	cout << "5 -> 2" << endl;
	update(5, 2);
	cout << "2 ~ 5 : " << getSection(2, 5) << endl;
	cout << "1 ~ 5 : " << getSection(1, 5) << endl;

	return 0;
}