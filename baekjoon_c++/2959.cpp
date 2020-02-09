// 2959

#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {

	int numbers[4];
	int S;

	for (int i = 0; i < 4; i++)
	{
		scanf("%d", &numbers[i]);
	}

	sort(numbers, numbers + 4);

	S = numbers[0] * numbers[2];

	printf("%d", S);

	return 0;
}