//Henry

#include<iostream>
using namespace std;

int main(void) {
	int T;
	int a, b;

	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cin >> a >> b;
		int x = 2;
		while (a*x - b !=1)
		{
			if (a==1)
			{
				cout << b << endl;
				break;
			}
			if (a*x - b>=0)
			{
				a = a * x - b;
				b = b*x;
				if (b%a==0)
				{
					b /= a;
					a = 1;
				}
				else
				{
					for (int i = 2; i < b; i++)
					{
						if (a%i==0 && b%i==0)
						{
							a /= i;
							b /= i;
						}
					}
				}
				x++;
			}
			else
			{
				x++;
			}
		}
		if(a!=1)
		cout << b * x << endl;
	}
	return 0;
}