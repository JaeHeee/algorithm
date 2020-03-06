#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int number[500000];


int main(void) {

	int N;
	double sum=0;
	int count[8001] = { 0, };
	int check[8001] = {0,};
	int maxList[8001] = { 0, };
	int maxListCount = 0;
	int maxCount;

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		scanf("%d", &number[i]);
		count[number[i]+4000]++;
		check[number[i]+4000]++;
		sum += number[i];
	}

	sort(number, number + N);
	sort(check, check + 8001);
	maxCount = check[8000];

	//1
	cout << long(round(sum / N)) << endl;

	//2
	printf("%d\n", number[N / 2]);

	//3
	for (int i = 0; i < 8001; i++)
	{
		if (maxCount == count[i]) {
			maxList[maxListCount] = i-4000;
			maxListCount++;
		}
	}
	sort(maxList, maxList + maxListCount);
	if (maxListCount>1)
	{
		printf("%d\n", maxList[1]);
	}
	else {
		printf("%d\n", maxList[0]);
	}

	//4
	printf("%d\n", number[N - 1] - number[0]);

	return 0;
}
