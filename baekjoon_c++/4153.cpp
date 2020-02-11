#include <iostream>
#include <algorithm>

using namespace std;


int main()
{
    int numbers[3];
    
    for(;;) {
        
        scanf("%d %d %d",&numbers[0],&numbers[1],&numbers[2]);
        
        if(numbers[0]==0 && numbers[1]==0 && numbers[2]==0) {
            break;
        }
        
        sort(numbers,numbers+3);
        if(numbers[2]*numbers[2] == numbers[1]*numbers[1]+numbers[0]*numbers[0]) {
            printf("right\n");
        } else {
            printf("wrong\n");
        }
    }
    
    return 0;    
}
