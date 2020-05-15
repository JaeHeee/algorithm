/*
��� ���� (Counting Sort)
	���� ������ �ִ� ��쿡 ���ؼ� ������ ���� �˰���
	ũ�⸦ �������� ������ ���� �˰���
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