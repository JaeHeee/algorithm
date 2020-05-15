/*
	KMP(knuth-Morris-Pratt) Algorithm
		문자열 매칭 알고리즘 - 특정한 글이 있을 때 그 글안에서 하나의 문자열을 찾는 알고리즘
		모든 경우를 다 비교하지 않아도 부분 문자열을 찾을 수 있는 알고리즘
		접두사와 접미사의 개념을 활용하여 반복되는 연산을 얼마나 줄일 수 있는지를 판별하여 매칭할 문자열을 빠르게 점프하는 기법
*/

#include <iostream>
#include <vector>

using namespace std;

vector<int> makeTable(string pattern) {
	int patternSize = pattern.size();
	vector<int> table(patternSize, 0);
	int j = 0;
	for (int i = 1; i < patternSize; i++)
	{
		while (j > 0 && pattern[i] != pattern[j]) {
			j = table[j - 1];
		}
		if (pattern[i] == pattern[j]) {
			table[i] = ++j;
		}
	}
	return table;
}

void KMP(string parent, string pattern) {
	vector<int> table = makeTable(pattern);
	int parentSize = parent.size();
	int patternSize = pattern.size();
	int j = 0;
	for (int i = 0; i < parentSize; i++)
	{
		while (j > 0 && parent[i] != pattern[j]) {
			j = table[j - 1];
		}
		if (parent[i] == pattern[j]) {
			if (j == patternSize - 1) {
				cout << i - patternSize + 2 << "번째에서 찾았습니다." << endl;
				j = table[j];
			}
			else {
				j++;
			}
		}
	}
}

int main(void) {
	string parent = "ababacabacaabacaaba";
	string pattern = "abacaaba";
	KMP(parent, pattern);
		
	return 0;
}