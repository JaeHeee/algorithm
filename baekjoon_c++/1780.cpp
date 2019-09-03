/*
	baekjoon #1780 종이의 개수
*/

#include <iostream>
#include <string>

using namespace std;

int number[2187][2187];
int answer[3];
int N;


string paper(int N,int row, int col) {
	if (N == 1)
	{
		return to_string(number[row][col] + 1);
	}

	string space[9];
	space[0] = paper(N / 3, row, col);
	space[1] = paper(N / 3, row, col+N/3);
	space[2] = paper(N / 3, row, col+N*2/3);
	space[3] = paper(N / 3, row+N/3, col);
	space[4] = paper(N / 3, row+N/3, col+N/3);
	space[5] = paper(N / 3, row+N/3, col + N * 2 / 3);
	space[6] = paper(N / 3, row + N * 2 / 3, col);
	space[7] = paper(N / 3, row + N * 2 / 3, col+N/3);
	space[8] = paper(N / 3, row + N * 2 / 3, col + N * 2 / 3);

	bool same = true;
	string value = space[0];
	for (int i = 0; i < 9; i++)
	{
		if (space[i] != value)
		{
			same = false;
		}
	}
	if (same && space[0].length() == 1) {
		return space[0];
	}

	string result = "(";
	for (int i = 0; i < 9; i++)
	{
		result += space[i];
	}
	result += ")";

	return result;
}

int main(void) {
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> number[i][j];
		}
	}

	string result = paper(N, 0, 0);
	for (int i = 0; i < result.length(); i++)
	{
		if (result[i] == '0') answer[0]++;
		if (result[i] == '1') answer[1]++;
		if (result[i] == '2') answer[2]++;
	}

	cout << answer[0] << endl << answer[1] << endl << answer[2];

	return 0;
}