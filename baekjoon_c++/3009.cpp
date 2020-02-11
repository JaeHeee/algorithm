#include <iostream>

using namespace std;

int countX[1001];
int countY[1001];

int main()
{
    int x;
    int y;
    int resultX;
    int resultY;
    
    for (int i = 0; i < 3; i++) {
        scanf("%d %d",&x,&y);
        countX[x]++;
        countY[y]++;
    }
    
    for (int i = 0; i < 1001; i++) {
        if(countX[i] == 1){
            resultX = i;
        }
        if(countY[i] == 1){
            resultY = i;
        }
    }
    
    printf("%d %d",resultX,resultY);

    return 0;    
}
