#include <iostream>
#include <algorithm>

using namespace std;


int main()
{
    int length[4];
    int check[4];
    
    scanf("%d %d %d %d",&length[0],&length[1],&length[2],&length[3]);
    
    check[0] = length[0];
    check[1] = length[1];
    check[2] = length[2] - length[0];
    check[3] = length[3] - length[1];
    
    sort(check,check+4);
    
    printf("%d",check[0]);
    
    return 0;    
}
