#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int E,S,M;
    bool check[3] = {false,false,false};
    int year=1;
    
    scanf("%d %d %d",&E,&S,&M);
    
    while(1){
        if(year%15==E || (year%15==0 &&E==15)){
            check[0] = true;
        }
        if(year%28==S || (year%28==0 &&S==28)){
            check[1] = true;
        }
        if(year%19==M || (year%19==0 &&M==19)){
            check[2] = true;
        }
        if(check[0]&&check[1]&&check[2]){
            break;
        }
        
        check[0] = false;
        check[1] = false;
        check[2] = false;
        
        year++;
    }
    
    printf("%d",year);
    
    return 0;
}
