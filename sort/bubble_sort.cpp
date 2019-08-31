/*
�������� (Bubble Sort) - �� ���ڸ� ���ؼ� �� ���� ���ڸ� ������ �����ش�.
O(N^2)
*/

#include <iostream>

using namespace std;

int main(void) {
	int temp;
	int numbers[10] = { 1,3,4,5,2,6,8,9,7,10 };

	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 9-i; j++)
		{
			if (numbers[j] > numbers[j+1])
			{
				temp = numbers[j];
				numbers[j] = numbers[j+1];
				numbers[j+1] = temp;
			}
		}
	}

	for (int i = 0; i < 10; i++)
	{
		cout << numbers[i] << " ";
	}


	return 0;
}

