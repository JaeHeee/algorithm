#include <iostream>

using namespace std;

int main()
{
    int T;
    
    while(1) {
        T--;
        int n,m;
        scanf("%d %d",&n,&m);
        if(n==0 && m==0){
            break;
        }
        printf("%d\n",n+m);
        
    }
    
    return 0;
}
