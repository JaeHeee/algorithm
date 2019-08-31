//Fibonacci numbers

#include <iostream>
using namespace std;

int main(void) {

	int number;
	int fib0 = 0;
	int fib1 = 1;
	int temp;

	cin >> number;

	if (number == 0)
	{
		cout << fib0 << endl;
	}
	else if (number == 1)
	{
		cout << fib1 <<endl;
	}
	else
	{
		for (int i = 0; i < number-1; i++)
		{
			temp = fib1;
			fib1 += fib0;
			fib0 = temp;
		}
		cout << fib1 << endl;
	}



	return 0;
}