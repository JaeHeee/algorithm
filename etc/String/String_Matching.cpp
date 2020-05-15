/*
	단순 비교 문자열 매칭 알고리즘
*/

#include <iostream>

using namespace std;

int findString(string parent, string pattern) {
	int parentSize = parent.size();
	int patternSize = pattern.size();
	for (int i = 0; i <= parentSize - patternSize; i++)
	{
		bool finded = true;
		for (int j = 0; j < patternSize; j++)
		{
			if (parent[i + j] != pattern[j])
			{
				finded = false;
				break;
			}
		}
		if (finded) {
			return i;
		}
	}
	return -1;
}


int main(void) {
	string parent = "Hello World";
	string pattern = "llo W";
	int result = findString(parent, pattern);
	if (result == -1) {
		cout << "Not found" << endl;
	}
	else {
		cout << "found : " << result + 1 << endl;
	}
		
	return 0;
}