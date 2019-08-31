#include <iostream>

using namespace std;

int main(void)
{
	int pay,number=0;
	int money = 1000;
	cin >> pay;

	money -= pay;
	while (money>0)
	{
		if (money >= 500)
		{
			number += (money / 500);
			money %= 500;
		}
		else if (money >= 100)
		{
			number += (money / 100);
			money %= 100;
		}
		else if (money >= 50)
		{
			number += (money / 50);
			money %= 50;
		}
		else if (money >= 10)
		{
			number += (money / 10);
			money %= 10;
		}
		else if (money >= 5)
		{
			number += (money / 5);
			money %= 5;
		}
		else if (money >= 1)
		{
			number += (money / 1);
			money = 0;
		}
	}
	
	cout << number <<endl; 

	return 0;
}