#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int N;
    int number;
    int result=0;
    vector<pair<int, int> > numbers;
    
    scanf("%d",&N);
    for (int i = 0; i < N; i++) {
        scanf("%d",&number);
        numbers.push_back(pair<int, int>(number,i));
    }
    
    sort(numbers.begin(),numbers.end());
    
    for (int i = 0; i < N; i++) {
        if(result<numbers[i].second-i) {
            result = numbers[i].second-i;
        }
    }
    
    printf("%d",result+1);
    
    return 0;
}
