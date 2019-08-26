/*
sort function basic
*/

#include <iostream>
#include <algorithm>

using namespace std;

void show(int* numbers) {
	for (int i = 0; i < 10; i++)
	{
		cout << numbers[i] << " ";
	}
}

bool compare(int a, int b)
{
	return a < b;
}

int main(void) {
	int numbers[10] = { 1,3,4,5,2,6,8,9,7,10 };
	sort(numbers, numbers + 10);
	show(numbers);

	cout << endl;

	int numbers2[10] = { 1,3,4,5,2,6,8,9,7,10 };
	sort(numbers2, numbers2 + 10, compare);
	show(numbers2);

	return 0;
}

