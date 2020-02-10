#include <iostream>

using namespace std;

int main()
{
    int T;
    
    scanf("%d",&T);
    
    for (int i = 0; i < T; i++) {
        int n,m;
        scanf("%d %d",&n,&m);
        printf("Case #%d: %d\n",i+1,n+m);
    }
    
    return 0;
}
