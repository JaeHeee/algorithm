/*
	baekjoon #1992 quad tree
*/

#include <iostream>
#include <string>

using namespace std;

char a[64][64];

string quad(int N,int row, int col) {
	if (N == 1) return string(1,a[row][col]);

	string one = quad(N/2,row,col);
	string two = quad(N / 2, row, col + N/2);
	string three = quad(N / 2, row + N / 2, col);
	string four = quad(N / 2, row + N / 2, col + N / 2);

	if (one == two && one == three && one == four && one.length() == 1)
	{
		return one;
	}
	else
	{
		return "(" + one + two + three + four + ")";
	}
}

int main(void) {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> a[i];
	}
	cout << quad(N,0,0);

	return 0;
}