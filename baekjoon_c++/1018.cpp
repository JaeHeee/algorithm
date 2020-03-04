#include <iostream>

using namespace std;

char board[50][50];

char whiteChess[8][8] = {
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'} };

char blackChess[8][8] = {
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'},
	{'B','W','B','W','B','W','B','W'},
	{'W','B','W','B','W','B','W','B'} };

int main(void) {

	int N,M;
	int result = -1;
	int whiteCount = 0;
	int blackCount = 0;

	

	scanf("%d %d",&N,&M);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> board[i][j];
		}
	}


	for (int i = 0; i < N-7; i++)
	{
		for (int j = 0; j < M-7; j++)
		{
			for (int k = 0; k < 8; k++)
			{
				for (int l = 0; l < 8; l++)
				{
					if (whiteChess[k][l] != board[i+k][j+l])
					{
						whiteCount++;
					}
					if (blackChess[k][l] != board[i+k][j+l])
					{
						blackCount++;
					}
				}
			}
			if (whiteCount <= blackCount)
			{
				if (whiteCount == 0)
				{
					result = 0;
				}
				else {
					if (result == -1)
					{
						result = whiteCount;
					}
					else {
						if (result > whiteCount)
						{
							result = whiteCount;
						}
					}
				}
			}
			else {
				if (blackCount == 0)
				{
					result = 0;
				}
				else {
					if (result == -1)
					{
						result = blackCount;
					}
					else {
						if (result > blackCount)
						{
							result = blackCount;
						}
					}
				}
			}
			whiteCount = 0;
			blackCount = 0;
		}
	}

	printf("%d", result);

	return 0;
}
