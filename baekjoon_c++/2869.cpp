#include <iostream>

using namespace std;


int main(void)
{
    int A, B, V;
    int day=0;

    scanf("%d %d %d",&A,&B,&V);
    
    if((V - B)%(A-B)==0) {
        day = (V - B)/(A-B);    
    } else {
        day = (V - B)/(A-B) + 1;
    }
    
    
    
    
    printf("%d",day);
    
    return 0;
}
