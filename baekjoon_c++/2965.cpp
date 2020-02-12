#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int point[3];
    int count=0;
    
    scanf("%d %d %d",&point[0],&point[1],&point[2]);
    
    while(1){
        if(point[2]-point[1]==1 && point[1]-point[0]==1){
            break;
        }
        if(point[1]-point[0] <= point[2]-point[1]) {
            point[0] = point[1]+1;
            sort(point,point+3);
            count++;
        } else {
            point[2] = point[1]-1;
            sort(point,point+3);
            count++;
        }
    }
    
    printf("%d",count);
    
    return 0;
}
