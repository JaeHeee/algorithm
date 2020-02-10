#include <iostream>

using namespace std;

int main()
{
    int H,M;
    
    scanf("%d %d",&H,&M);
    
    if(M >= 45) {
        M -=45;
    } else {
        if(H==0){
            H = 23;
        } else{
            H -= 1;
        }
        
        M = 60-(45-M);
    }
    
    printf("%d %d",H,M);
    
    return 0;
}
