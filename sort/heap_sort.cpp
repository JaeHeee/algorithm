/*
������ (Heap Sort)
	�� Ʈ�� ������ �̿��ϴ� ���� ���
	���� �ּڰ��̳� �ִ��� ������ ã�Ƴ��� ���� ���� ���� Ʈ���� ������� �ϴ� Ʈ��
	
	- �ִ���
		�θ��尡 �ڽĳ�庸�� ū ��
	
	- Heapify algorithm O(logN)
		Ư���� �ϳ��� ��忡 ���ؼ� ����.
		�ش� ��带 �����ϰ�� �ִ� ���� �����Ǿ� �ִ� ���¶�� �����Ѵ�.
		Ư���� ����� �� �ڽ� �߿��� �� ū �ڽİ� �ڽ��� ��ġ�� �ٲٴ� �˰���

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
	// heap ������ �ٲ��ش�.
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