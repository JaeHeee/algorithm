/*
계수 정렬 (Counting Sort)
	범위 조건이 있는 경우에 한해서 굉장히 빠른 알고리즘
	크기를 기준으로 갯수를 세는 알고리즘
	O(N)
*/

#include <iostream>

using namespace std;

int main(void) {

	int count[5] = { 0, };
	int numbers[30] = {
		1,3,4,2,5,1,2,3,4,1,
		1,1,2,3,4,5,1,2,3,4,
		5,5,2,2,4,3,2,1,4,1
	};
	int temp;

	for (int i = 0; i < 30; i++)
	{
		count[numbers[i] - 1]++;
	}

	for (int i = 0; i < 5; i++)
	{
		if (count[i]!=0)
		{
			for (int j = 0; j < count[i]; j++)
			{
				cout << i + 1 << " ";
			}
		}
	}

	return 0;
}