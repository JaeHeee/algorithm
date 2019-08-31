#include <iostream>
#include <string>

using namespace std;

string input;

int main(void)
{	
	int result = 0;
	string temp = "";
	int minus = 0;

	cin >> input;

	for (int i = 0; i <= input.size(); i++)
	{
		if (input[i] == '+' || input[i] == '-' || input[i] == '\0')
		{
			if (minus == 1)
			{
				result += -stoi(temp);
			}
			else
			{
				result += stoi(temp);
			}
			temp = "";
			if (input[i] == '-')
			{
				minus = 1;
			}
			continue;
		}
		temp += input[i];
	}

	cout << result;
	return 0;
}