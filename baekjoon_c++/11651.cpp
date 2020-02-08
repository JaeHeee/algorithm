#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(pair<int, int> a,
	pair<int, int> b) {
	if (a.second == b.second)
	{
		return a.first < b.first;
	}
	else
	{
		return a.second < b.second;
	}
}

int main(void) {

	int N;
	vector<pair<int,int> > points;
	
	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		int x;
		int y;
		scanf("%d", &x);
		scanf("%d", &y);

		points.push_back(pair<int, int>(x, y));

	}
	   
	sort(points.begin(), points.end(), compare);

	for (int i = 0; i < N; i++)
	{
		printf("%d %d\n",points[i].first,points[i].second);
	}


	return 0;
}