#include <iostream>

using namespace std;

int a[10000];

int main()
{
    int n,m;
    int sum = 0;
    int min = 10001;
    
    
    scanf("%d %d",&n,&m);
    
    for (int i = 2; i <= m; i++) {
        a[i] = i;
    }
    for (int i = 2; i <= m; i++) {
        if(a[i]==0) continue;
        for (int j = i+i; j <= m; j+=i) {
            a[j]=0;
        }
    }
    for (int i = n; i <= m; i++) {
        if(a[i]!=0){
            sum += a[i];
            if(min>a[i]) {
                min = a[i];
            }
        }
    }
    
    if(sum==0){
        printf("-1");
    } else {
        printf("%d\n%d",sum,min);
    }
    
    return 0;    
}
