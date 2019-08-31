/*
퀵정렬 (Quick Sort)
	분할정복 알고리즘
	특정한 값을 기준으로 큰 숫자와 작은 숫자를 서로 교환한 뒤 배열을 반으로 나눈다.
	평균 : O(N*logN)
	최악 : O(n^2) 이미 정렬되어있는 경우
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

