/*
sort function pair
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool compare(pair<string, pair<int, int>>a, pair<string, pair<int, int>>b) {
	if (a.second.first == b.second.first)
	{
		return a.second.second > b.second.second;
	}
	else
	{
		return a.second.first > b.second.first;
	}
}

int main(void) {
	vector<pair<int, string> > v;
	v.push_back(pair<int, string> (90,"kim"));
	v.push_back(pair<int, string> (87, "park"));
	v.push_back(pair<int, string> (92,"lee"));

	sort(v.begin(), v.end());
	for (int i = 0; i < v.size(); i++)
	{
		cout << v[i].second << endl;
	}

	vector<pair<string, pair<int,int>>> v2;
	v2.push_back(pair<string, pair<int, int>>("kim",pair<int, int>(90,19940927)));
	v2.push_back(pair<string, pair<int, int>>("park",pair<int, int>(85, 19940121)));
	v2.push_back(pair<string, pair<int, int>>("lee", pair<int, int>(85, 19950221)));
	v2.push_back(pair<string, pair<int, int>>("na", pair<int, int>(95, 19940121)));

	sort(v2.begin(), v2.end(),compare);
	for (int i = 0; i < v2.size(); i++)
	{
		cout << v2[i].first<< endl;
	}

	return 0;
}

