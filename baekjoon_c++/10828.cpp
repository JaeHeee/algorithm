//Stack
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(void) {

	int count;
	cin >> count;
	string input;
	
	stack<int> stack;

	for (int i = 0; i < count; i++)
	{
		cin >> input;
		
		if (input == "push")
		{
			int number;
			cin >> number;
			stack.push(number);
		}
		else if (input == "pop")
		{
			if (stack.empty())
			{
				cout << "-1" << endl;
			}
			else
			{
				cout << stack.top() << endl;
				stack.pop();
			}
		}
		else if (input == "size")
		{
			cout << stack.size() << endl;
		}
		else if (input == "empty")
		{
			if (stack.empty())
			{
				cout << true << endl;
			}
			else
			{
				cout << false << endl;
			}
		}
		else if (input == "top")
		{
			if (stack.empty())
			{
				cout << "-1" << endl;
			}
			else
			{
				cout << stack.top() << endl;
			}
		}
	}

	return 0;
}