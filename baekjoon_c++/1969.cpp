#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string DNA[1001];
string ACGT = "ACGT";
int nucle[4] = { 0, };

int main(void)
{
	int N;
	int M;
	string DNA_s;
	cin >> N >> M;
	
	for (int i = 0; i < N; i++)
	{
		cin >> DNA[i];
	}

	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (DNA[j][i]=='A')
			{
				nucle[0] += 1;
			}
			else if (DNA[j][i] == 'C')
			{
				nucle[1] += 1;
			}
			else if (DNA[j][i] == 'G')
			{
				nucle[2] += 1;
			}
			else if (DNA[j][i] == 'T')
			{
				nucle[3] += 1;
			}
		}
		int max = nucle[0];
		int index = 0;
		for (int k = 1; k < 4; k++)
		{
			if (nucle[k] > max)
			{
				max = nucle[k];
				index = k;
			}
		}
		DNA_s += ACGT[index];
		nucle[0] = 0;
		nucle[1] = 0;
		nucle[2] = 0;
		nucle[3] = 0;
	}

	int min = 0;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (DNA_s[j] != DNA[i][j])
			{
				min += 1;
			}
		}
	}

	cout <<DNA_s << endl << min << endl;

	return 0;
}