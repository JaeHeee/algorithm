#include <iostream>

using namespace std;

int main()
{
    int numbers[9];
    int max=0;
    int result;
    
    for (int i = 0; i < 9; i++) {
        scanf("%d",&numbers[i]);
    }
    
    for (int i = 0; i < 9; i++) {
        if(max < numbers[i]){
            max = numbers[i];
            result = i;
        }
    }
    
    printf("%d\n%d",max,result+1);
    
    
    
    return 0;
}
