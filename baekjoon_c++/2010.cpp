#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    int plug[500000];
    int result=1;
    
    scanf("%d",&N);
    
    for (int i = 0; i < N; i++) {
        scanf("%d",&plug[i]);
    }
    
    sort(plug,plug+N);
    
    if(plug[N-1]==1) {
        printf("%d",1);
    } else{
        for (int i = N-1; i >= 0; i--) {
            result += (plug[i]-1);
        }
        printf("%d",result);
    }
    
    return 0;
}
