/*
선택정렬 (Selection Sort) - 가장 작은것을 제일 앞으로
O(N^2)
*/

#include <iostream>

using namespace std;

int main(void) {
	int min, index, temp;
	int numbers[10] = { 1,3,4,5,2,6,8,9,7,10 };
	
	for (int i = 0; i < 10; i++)
	{
		min = 10000;
		for (int j = i; j < 10; j++)
		{
			if (min > numbers[j])
			{
				min = numbers[j];
				index = j;
			}
		}
		temp = numbers[i];
		numbers[i] = numbers[index];
		numbers[index] = temp;
	}

	for (int i = 0; i < 10; i++)
	{
		cout << numbers[i] << " ";
	}


	return 0;
}

