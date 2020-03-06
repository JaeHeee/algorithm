#include <iostream>
#include <algorithm>

using namespace std;

int burger[3];
int drink[2];

int main(void) {

	for (int i = 0; i < 3; i++)
	{
		scanf("%d", &burger[i]);
	}
	for (int i = 0; i < 2; i++)
	{
		scanf("%d", &drink[i]);
	}

	sort(burger, burger + 3);
	sort(drink, drink + 2);

	printf("%d", burger[0] + drink[0] - 50);



	return 0;
}
