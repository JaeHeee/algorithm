/*
������ (Quick Sort)
	�������� �˰���
	Ư���� ���� �������� ū ���ڿ� ���� ���ڸ� ���� ��ȯ�� �� �迭�� ������ ������.
	��� : O(N*logN)
	�־� : O(n^2) �̹� ���ĵǾ��ִ� ���
*/

#include <iostream>

using namespace std;

int numbers[10] = { 1,3,4,5,2,6,8,9,7,10 };

void show() {
	for (int i = 0; i < 10; i++)
	{
		cout << numbers[i] << " ";
	}
}

void quick_sort(int* numbers, int start, int end) {
	if (start >= end)
	{
		return;
	}

	int key = start;
	int i = start + 1;
	int j = end;
	int temp;

	while (i <= j)
	{
		while (i <= end && numbers[i] <= numbers[key])
		{
			i++;
		}
		while (j > start && numbers[j] >= numbers[key])
		{
			j--;
		}
		if (i> j)
		{
			temp = numbers[j];
			numbers[j] = numbers[key];
			numbers[key] = temp;
		}
		else
		{
			temp = numbers[i];
			numbers[i] = numbers[j];
			numbers[j] = temp;
		}
	}

	quick_sort(numbers, start, j - 1);
	quick_sort(numbers, j + 1, end);
}

int main(void) {

	quick_sort(numbers, 0, 9);
	show();
	return 0;
}

