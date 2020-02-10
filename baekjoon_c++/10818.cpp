#include <iostream>

using namespace std;

int main()
{
    int numbers[1000000];
    int max=-1000000;
    int min=1000000;
    int N;
    
    scanf("%d",&N);
    
    for (int i = 0; i < N; i++) {
        scanf("%d",&numbers[i]);
    }
    
    for (int i = 0; i < N; i++) {
        if(max < numbers[i]){
            max = numbers[i];
    }
        if(min > numbers[i]){
            min = numbers[i];
        }
    }
    
    printf("%d %d",min,max);
    
    
    
    return 0;
}
