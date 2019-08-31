/*
병합정렬 (Merge Sort)
	분할정복 알고리즘
	정확히 반절씩 나눈다는 점에서 최악의 경우에도 O(N*logN)
	기존의 데이터를 담을 추가적인 배열 공간이 필요
	O(N*logN)
*/

#include <iostream>

using namespace std;

int sorted[10];

void show(int* numbers) {
	for (int i = 0; i < 10; i++)
	{
		cout << numbers[i] << " ";
	}
}

void merge(int *numbers, int m, int middle, int n) {
	int i = m;
	int j = middle + 1;
	int k = m;

	while (i <= middle && j <= n)
	{
		if (numbers[i] < numbers[j])
		{
			sorted[k] = numbers[i];
			i++;
		}
		else
		{
			sorted[k] = numbers[j];
			j++;
		}
		k++;
	}

	if (i>middle)
	{
		for (int a = j; a <= n ; a++)
		{
			sorted[k] = numbers[a];
			k++;
		}
	}
	else
	{
		for (int a = i; a <= middle; a++)
		{
			sorted[k] = numbers[a];
			k++;
		}
	}

	for (int a = m; a <= n; a++)
	{
		numbers[a] = sorted[a];
	}
}

void merge_sort(int* numbers, int m, int n) {
	if (m < n)
	{
		int middle = (m + n) / 2;
		merge_sort(numbers, m, middle);
		merge_sort(numbers, middle + 1, n);
		merge(numbers, m, middle, n);
	}
}

int main(void) {
	int numbers[10] = { 1,3,4,5,2,6,8,9,7,10 };

	merge_sort(numbers, 0, 9);
	show(numbers);
	return 0;
}

