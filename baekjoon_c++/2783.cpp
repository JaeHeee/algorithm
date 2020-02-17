#include <iostream>

using namespace std;

int main()
{
    double X,Y;
    int N;
    double min;
    
    scanf("%d %d",&X,&Y);
    scanf("%d",&N);
    
    min = X/Y;
    
    for (int i = 0; i < N; i++) {
        scanf("%d %d",&X,&Y);
        if(min > X/Y) {
            min = X/Y;
        }
    }
    
    cout<<min*1000;

    return 0;
}
