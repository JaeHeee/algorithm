/*
	Binary Search
	이미 데이터가 정렬이 되어 있는 상황에서 범위를 반씩 좁혀가며 데이터를 빠르게 탐색하는 알고리즘
*/

#include <iostream>
#define NUMBER 12

using namespace std;

int numbers[] = { 1,3,5,7,9,11,14,15,18,19,25,28 };


int search(int start, int end, int target) {
	if (start > end) return -1;
	int mid = (start + end) / 2;
	if (numbers[mid] == target) return mid;
	else if (numbers[mid] > target) return search(start, mid - 1, target);
	else return search(mid + 1, end, target);
}

int main(void) {
	int data = 7;
	int result = search(0, NUMBER - 1,data);
	if (result != -1)
		cout << result + 1 << endl;

	return 0;
}