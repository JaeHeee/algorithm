
#include <iostream>
#include <string>
using namespace std;

int main(void) {
	int test;
	int number;
	string dress;
	
	cin >> test;
	for (int i = 0; i < test; i++)
	{
		string name[30];
		int count[30] = { 0, };
		int total = 1;
		int same;
		cin >> number;
		cin.ignore();

		for (int j = 0; j < number; j++)
		{
			same = 0;
			getline(cin, dress);
			dress.erase(0, dress.find(" ")+1);
			for (int k = 0; k < number; k++)
			{
				if (dress.compare(name[k])==0)
				{
					count[k] += 1;
					same = 1;
					break;
				}
			}
			if (same == 0)
			{
				name[j] = dress;
				count[j] = 1;
			}
		}
		
		if (number == 0)
		{
			cout << number << endl;
		}
		else if (count[0] == number)
		{
			cout << number << endl;
		}
		else
		{
			for (int m = 0; m < number; m++)
			{
				if (count[m]!=0)
				{
					count[m] += 1;
					total *= count[m];
				}
			}
			cout << total -1 << endl;
		}
	}
	

	return 0;
}