#include <iostream>
#include <string>
#include <vector>

using namespace std;

string number;
vector<char> v;

int main(void)
{
	string result;
	int N;
	int K;
	cin >> N >> K;
	cin >> number;
	v.push_back(0);

	for (int i = 0; i < N; i++)
	{
		while (K > -1 && !v.empty() && v.back() < number[i])
		{
			v.pop_back();
			K--;
		}
		v.push_back(number[i]);
	}

	while (K>-1)
	{
			v.pop_back();
			K--;
	}
	
	for (int i = 0; i < v.size(); i++)
	{
		result += v[i];
	}

	cout << result;

	return 0;
}