/*
삽입정렬 (Insertion Sort)
	각 숫자를 적절한 위치에 삽입
	데이터가 이미 거의 정렬된 상태에 한해서는 어떤 알고리즘보다도 빠르다
	O(N^2)
*/

#include <iostream>

using namespace std;

int main(void) {
	int temp;
	int numbers[10] = { 1,3,4,5,2,6,8,9,7,10 };

	for (int i = 0; i < 9; i++)
	{
		j = i;
		while (j >=0 && numbers[j] > numbers[j+1])
		{
			temp = numbers[j];
			numbers[j] = numbers[j + 1];
			numbers[j + 1] = temp;
			j--;
		}
	}

	for (int i = 0; i < 10; i++)
	{
		cout << numbers[i] << " ";
	}


	return 0;
}

