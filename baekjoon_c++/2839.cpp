#include <iostream>

using namespace std;

int main()
{
    int n;
    int a,b;
    int result = -1;

    scanf("%d",&n);
    
    a = n/5;
    
    for (int i = a; i >= 0; i--) {
        b = n-5*i;
        if(b%3==0) {
            result = i+b/3;
            break;
        }
    }
    
    printf("%d",result);
    
    
    return 0;    
}
