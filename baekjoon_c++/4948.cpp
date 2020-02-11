#include <iostream>

using namespace std;

int a[300000];

int main()
{
    int n;
    
    for (;;) {
        int count = 0;
        scanf("%d",&n);
        if(n==0){
            break;
        }
        
        for (int i = 2; i <= 2*n; i++) {
            a[i] = i;
        }
        for (int i = 2; i <= 2*n; i++) {
            if(a[i]==0) continue;
            for (int j = i+i; j <= 2*n; j+=i) {
                a[j]=0;
            }
        }
        for (int i = n+1; i <= 2*n; i++) {
            if(a[i]!=0){
                count++;
            }
        }
        
        printf("%d\n",count);
    }
    
    return 0;    
}
