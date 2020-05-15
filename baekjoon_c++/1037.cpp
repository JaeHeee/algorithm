#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    int number[50];
    
    scanf("%d",&N);
    
    for (int i = 0; i < N; i++) {
        scanf("%d",&number[i]);
    }
    
    sort(number,number+N);
    
    if(N%2==0){
        printf("%d",number[0]*number[N-1]);
    } else {
        printf("%d",number[N/2]*number[N/2]);
    }
    
    return 0;
}
