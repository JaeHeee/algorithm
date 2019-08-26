/*
힙정렬 (Heap Sort)
	힙 트리 구조를 이용하는 정렬 방법
	힙은 최솟값이나 최댓값을 빠르게 찾아내기 위해 완전 이진 트리를 기반으로 하는 트리
	
	- 최대힙
		부모노드가 자식노드보다 큰 힙
	
	- Heapify algorithm O(logN)
		특정한 하나의 노드에 대해서 수행.
		해당 노드를 제외하고는 최대 힙이 구성되어 있는 상태라고 가정한다.
		특정한 노드의 두 자식 중에서 더 큰 자식과 자신의 위치를 바꾸는 알고리즘

	O(N*logN)
*/

#include <iostream>

using namespace std;

int heap[9] = { 2,3,1,4,7,8,6,9,5 };

void show(int* numbers) {
	for (int i = 0; i < 9; i++)
	{
		cout << numbers[i] << " ";
	}
}

int main(void) {
	// heap 구조로 바꿔준다.
	for (int i = 1; i < 9; i++)
	{
		int c = i;
		do
		{
			int root = (c - 1) / 2;
			if (heap[root] < heap[c])
			{
				int temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			}
			c = root;
		} while (c != 0);
	}

	for (int i = 9-1 ; i >= 0; i--)
	{
		int temp = heap[0];
		heap[0] = heap[i];
		heap[i] = temp;
		int root = 0;
		int c = 1;
		do
		{
			c = 2 * root + 1;
			if (heap[c] < heap[c+1] && c<i-1)
			{
				c++;
			}
			if (heap[root] < heap[c] && c<i)
			{
				int temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			}
			root = c;
		} while (c < i);
	}



	show(heap);

	return 0;
}