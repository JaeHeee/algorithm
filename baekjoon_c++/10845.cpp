//Queue
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main(void) {

	int count;
	cin >> count;
	string input;

	queue<int> queue;

	for (int i = 0; i < count; i++)
	{
		cin >> input;

		if (input == "push")
		{
			int number;
			cin >> number;
			queue.push(number);
		}
		else if (input == "pop")
		{
			if (queue.empty())
			{
				cout << "-1" << endl;
			}
			else
			{
				cout << queue.front() << endl;
				queue.pop();
			}
		}
		else if (input == "size")
		{
			cout << queue.size() << endl;
		}
		else if (input == "empty")
		{
			if (queue.empty())
			{
				cout << true << endl;
			}
			else
			{
				cout << false << endl;
			}
		}
		else if (input == "front")
		{
			if (queue.empty())
			{
				cout << "-1" << endl;
			}
			else
			{
				cout << queue.front() << endl;
			}
		}
		else if (input == "back")
		{
			if (queue.empty())
			{
				cout << "-1" << endl;
			}
			else
			{
				cout << queue.back() << endl;
			}
		}
	}

	return 0;
}