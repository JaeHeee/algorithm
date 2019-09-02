/*
	다이나믹프로그래밍(Dynamic Programming)
	하나의 문제는 한 번만 풀도록 하는 알고리즘
	가정1) 큰 문제를 작은 문제로 나눌 수 있다.
	가정2) 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
	메모이제이션 이미 계산한 결과를 기록
	
	피보나치
*/

#include <iostream>

using namespace std;

int d[100];

int fibonacci(int x) {
	if (x == 1) return 1;
	if (x == 2) return 1;
	if (d[x] != 0) return d[x];
	return d[x] = fibonacci(x - 1) + fibonacci(x - 2);
}

int main(void) {

	cout << fibonacci(30) << endl;

	return 0;
}