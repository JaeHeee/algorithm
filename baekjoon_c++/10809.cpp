//¾ËÆÄºª¹®Á¦
#include <iostream>
#include <cstring>
using namespace std;

int main(void) {

	int alphabet[26];
	char word[100];
	int index;
	cin >> word;

	for (int i = 0; i < 26; i++)
	{
		alphabet[i] = -1;
	}

	for (int i = 0; i < strlen(word); i++)
	{
		index = word[i] - 97;
		if (alphabet[index] == -1)
		{
			alphabet[index] = i;
		}
	}

	for (int i = 0; i < 26; i++)
	{
		cout << alphabet[i]<<" ";
	}

	return 0;
}
