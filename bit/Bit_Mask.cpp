/*
	비트 마스크(Bit Mask)
		메모리를 적게 사용할 수 있다.
		프로그램이 더욱 빠르게 동작한다.
		소스코드가 직관적으로 변경된다.
*/

#include <iostream>

using namespace std;

void show(int *a) {
	for (int i = 32; i > 0; i--)
	{
		cout << ((*a & (1<< i - 1)) ? 1 : 0);
	}
}

void init(int *a) {
	*a = 0;
}

void full(int *a) {
	*a = -1;
}

void drop(int *a, int i) {
	*a &= ~(1 << i);
}

void set(int *a, int i) {
	*a |= (1 << i);
}

bool isSet(int *a, int i) {
	return *a & (1 << i);
}

void toggle(int *a, int i) {
	*a ^= (1 << i);
}

int getLast(int *a) {
	return (*a & -*a);
}

void dropLast(int *a) {
	*a &= (*a - 1);
}

int main(void) {
	int a;
	
	init(&a);
	cout << "모든 원소 삭제 : ";
	show(&a);
	cout << endl;

	full(&a);
	cout << "모든 원소 포함 : ";
	show(&a);
	cout << endl;

	drop(&a, 5);
	cout << "5번 인덱스 삭제 : ";
	show(&a);
	cout << endl;

	set(&a, 5);
	cout << "5번 인덱스 포함 : ";
	show(&a);
	cout << endl;

	cout << "5번 인덱스 포함 여부 : " << isSet(&a, 5);
	cout << endl;

	toggle(&a, 5);
	cout << "5번 인덱스 토글 : ";
	show(&a);
	cout << endl;

	cout << "5번 인덱스 포함 여부 : " << isSet(&a, 5);
	cout << endl;

	dropLast(&a);
	show(&a);
	cout << endl;
	dropLast(&a);
	show(&a);
	cout << endl;
	dropLast(&a);

	cout << "마지막 원소 3개 삭제 : ";
	show(&a);
	cout << endl;

	cout << "마지막 원소 구하기 : " << getLast(&a);
	cout << endl;

	return 0;
}