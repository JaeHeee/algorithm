#include <iostream>

using namespace std;

int apartment[15][15];

int main()
{
    int T;
    int k,n;
    scanf("%d",&T);
    
    for (int i = 0; i < 15; i++) {
        apartment[0][i] = i;
        apartment[i][1] = 1;
    }
    
    for (int i = 0; i < T; i++) {
        scanf("%d %d",&k,&n);
        for (int i = 1; i <= k; i++) {
            for (int j = 2; j <= n; j++) {
                apartment[i][j] = apartment[i-1][j] + apartment[i][j-1];
            }
        }
        
        printf("%d\n",apartment[k][n]);
    }
    
    return 0;    
}
