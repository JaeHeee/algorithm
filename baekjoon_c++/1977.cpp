#include <iostream>
#include <algorithm>

using namespace std;

int number[10000];

int main()
{
    int m,n;
    int size=0;
    int sum=0;
    
    scanf("%d %d",&m,&n);
    
    for (int i = m; i <= n; i++) {
        for (int j = 1; j <= 100; j++) {
            if(i/j == j && i%j == 0) {
                number[size] = i;
                size+=1;
                break;
            }
        }
    }
    
    sort(number,number+size);
    
    for (int i = 0; i < size; i++) {
        sum += number[i];
    }
    if(sum==0){
        printf("-1");
    } else{
        printf("%d\n%d",sum,number[0]);    
    }
    
    
    return 0;
}
