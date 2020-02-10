#include <iostream>

using namespace std;

int main()
{
    int num1;
    int num2;
    
    scanf("%d %d",&num1,&num2);
    
    if(num1 < num2){
        printf("<");
    } else if(num1 > num2) {
        printf(">");
    } else{
        printf("==");
    }
    
    return 0;
}
