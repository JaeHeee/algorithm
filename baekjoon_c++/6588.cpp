/*
	6588번 골드바흐의 추측
*/
#include <iostream>
#include <cstdio>
#define MAX 1000001

using namespace std;

int a[MAX];

int main(void) {
	a[1] = 1;
	for (int i = 2; i <= MAX; i++)
	{
		for (int j = i * 2; j <= MAX; j += i) {
			if (a[j] == 1) {
				continue;
			}
			else {
				a[j] = 1;
			}
		}
	}

	while (1)
	{
		int number;
		scanf("%d", &number);
		if (number == 0)
		{
			break;
		}
		bool find = false;
		for (int i = number; i >= number / 2; i--)
		{
			if (a[i] == 0 && a[number - i] == 0) {
				printf("%d = %d + %d\n", number, number - i, i);
				find = true;
				break;
			}
		}
		if (!find) {
			printf("Goldbach's conjecture is wrong.\n");
		}
	}

	return 0;

}