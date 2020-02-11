#include <iostream>
#include <algorithm>

using namespace std;


int main()
{
    int X;
    int before[2]={1,1};
    int after[2]={1,1};
    
    scanf("%d",&X);
    
    for (int i = 1; i < X; i++) {
        if(after[0]==1 && after[1]%2!=0){
            before[0]=after[0];
            before[1]=after[1];
            after[1]+=1;
        } else if(after[0]==1 && after[1]%2==0){
            before[0]=after[0];
            before[1]=after[1];
            after[0]+=1;
            after[1]-=1;
        } else if(after[0]%2==0 && after[1]==1) {
            before[0]=after[0];
            before[1]=after[1];
            after[0]+=1;
        } else if(after[0]%2!=0 && after[1]==1){
            before[0]=after[0];
            before[1]=after[1];
            after[0]-=1;
            after[1]+=1;
        } else if(before[0]%2!=0 && before[1]==1){
            after[0]-=1;
            after[1]+=1;
        } else if(before[0]==1 && before[1]%2==0){
            after[0]+=1;
            after[1]-=1;
        }
    }
    
    printf("%d/%d",after[0],after[1]);
    
    return 0;    
}
