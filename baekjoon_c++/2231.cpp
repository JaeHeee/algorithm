#include <iostream>

using namespace std;

int main(void) {

	int N;
	int check = false;
	int creator;
	int sum = 0;

	scanf("%d", &N);

	for (int i = 1; i < 999955; i++)
	{
		if (i<10) {
			sum = i + i;
			if (sum == N) {
				creator = i;
				check = true;
				break;
			}
		}
		else if (i < 100) {
			sum = i + i / 10 + i % 10;
			if (sum==N)
			{
				creator = i;
				check = true;
				break;
			}
		}
		else if (i < 1000) {
			sum = i + i / 100 + (i%100)/10 + i%10;
			if (sum == N)
			{
				creator = i;
				check = true;
				break;
			}
		}
		else if (i < 10000) {
			sum = i + i/1000 + (i%1000)/100 + (i%100)/10 + i%10;
			if (sum == N)
			{
				creator = i;
				check = true;
				break;
			}
		}
		else if (i < 100000) {
			sum = i + i / 10000 + (i%10000)/1000 + (i % 1000) / 100 + (i % 100) / 10 + i % 10;
			if (sum == N)
			{
				creator = i;
				check = true;
				break;
			}
		}
		else {
			sum = i + i/100000 + (i%100000)/10000 + (i%10000) / 1000 + (i % 1000) / 100 + (i % 100) / 10 + i % 10;
			if (sum == N)
			{
				creator = i;
				check = true;
				break;
			}
		}
	}

	if (check) {
		printf("%d", creator);
	}
	else
	{
		printf("0");
	}


	return 0;
}
