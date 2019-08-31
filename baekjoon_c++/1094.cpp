//bar

#include<iostream>
using namespace std;

int main(void) {
	int length = 64;
	int x;
	int number = 0;

	cin >> x;

	while (x>0)
	{
		if (length > x)
		{
			length /= 2;
		}
		else
		{
			number++;
			x -= length;
		}
	}

	cout << number << endl;

	return 0;
}