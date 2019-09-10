/*
	이진트리 구현과 순회 알고리즘
	
	- 전위순회(Preorder Traversal)
		1. 자기 자신 처리
		2. 왼쪽 자식 방문
		3. 오른쪽 자식 방문

	- 중위순회(Inorder Traversal)
		1. 왼쪽 자식 방문
		2. 자기 자신 처리
		3. 오른쪽 자식 방문

	- 후위순회(Postorder Traversal)
		1. 왼쪽 자식 방문
		2. 오른쪽 자식 방문
		3. 자기 자신 처리
*/

#include <iostream>

using namespace std;

const int number = 15;

typedef struct node *treePointer;
typedef struct node {
	int data;
	treePointer leftChild, rightChild;
} node;

void preorder(treePointer ptr) {
	if (ptr) {
		cout << ptr->data << ' ';
		preorder(ptr->leftChild);
		preorder(ptr->rightChild);
	}
}

void inorder(treePointer ptr) {
	if (ptr) {
		inorder(ptr->leftChild);
		cout << ptr->data << ' ';
		inorder(ptr->rightChild);
	}
}

void postorder(treePointer ptr) {
	if (ptr) {
		postorder(ptr->leftChild);
		postorder(ptr->rightChild);
		cout << ptr->data << ' ';
	}
}

int main(void) {
	node nodes[number + 1];
	for (int i = 1; i <= number; i++)
	{
		nodes[i].data = i;
		nodes[i].leftChild = NULL;
		nodes[i].rightChild = NULL;
	}

	for (int i = 1; i <= number; i++)
	{
		if (i % 2 == 0) {
			nodes[i / 2].leftChild = &nodes[i];
		}
		else {
			nodes[i / 2].rightChild = &nodes[i];
		}
	}

	preorder(&nodes[1]);
	cout << '\n';
	inorder(&nodes[1]);
	cout << '\n';
	postorder(&nodes[1]);

	return 0;
}
