#include <iostream>

using namespace std;

int numbers[42];

int main()
{
    int count=0;
    
    for (int i = 0; i < 10; i++) {
        int num;
        scanf("%d",&num);
        numbers[num%42]++ ;
    }
    
    for (int i = 0; i < 42; i++) {
        if(numbers[i] != 0){
            count++;
        }
    }
    
    printf("%d",count);

    return 0;
}
