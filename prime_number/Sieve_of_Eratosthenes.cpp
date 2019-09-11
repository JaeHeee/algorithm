/*
	소수판별 알고리즘
	에라토스테네스의 체 - 대량의 소수를 한꺼번에 판별
*/

#include <iostream>

using namespace std;

int number = 100000;
int numbers[100001];

void primeNumber() {
	for (int i = 2; i <= number; i++)
	{
		numbers[i] = i;
	}

	for (int i = 2; i <= number; i++)
	{
		if (numbers[i] == 0) continue;
		for (int j = i+i; j <= number; j+=i)
		{
			numbers[j] = 0;
		}
	}

	for (int i = 2; i <= number; i++) {
		if (numbers[i] != 0)
			cout << numbers[i] << endl;
	}
}

int main(void) {

	primeNumber();

	return 0;
}
