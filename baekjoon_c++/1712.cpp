#include <iostream>

using namespace std;

int main()
{
    int a,b,c;
    int n=1;
    
    scanf("%d %d %d",&a,&b,&c);
    
    if(c<=b){
        printf("-1");
    } else {
        while(1) {
            if(n> a/(c-b)) {
                printf("%d",n);
                break;
            }
            n++;
        }
    }
    
    return 0;
}
