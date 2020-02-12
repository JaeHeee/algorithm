#include <iostream>

using namespace std;

int sum[5];
int score[5][4];

int main()
{
    
    int max=0;
    int number;
    
    
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 4; j++) {
            scanf("%d",&score[i][j]);
            sum[i] += score[i][j];
        }
    }
    
    for (int i = 0; i < 5; i++) {
        if(max<sum[i]){
            max = sum[i];
            number = i+1;
        }
    }
    
    printf("%d %d",number,max);

    return 0;
}
