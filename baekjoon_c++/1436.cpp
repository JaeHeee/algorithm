#include <iostream>
#include <string>

using namespace std;

int main(void) {

	int N;
	string check;

	scanf("%d",&N);

	for (int i = 666; N > 0; i++)
	{
		check = to_string(i);
		if (check.find("666") != -1) {
			N--;
		}
	}

	cout << check << endl;

	return 0;
}
