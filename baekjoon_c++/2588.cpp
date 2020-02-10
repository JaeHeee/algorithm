#include <iostream>

using namespace std;

int main()
{
    int num1;
    int num2;
    int result1;
    int result2;
    int result3;
    
    scanf("%d %d",&num1,&num2);
    
    result1 = num1*(num2%10);
    result2 = num1*((num2%100)/10);
    result3 = num1*(num2/100);
    
    printf("%d\n",result1);
    printf("%d\n",result2);
    printf("%d\n",result3);
    printf("%d\n",result1+result2*10+result3*100);
    
    return 0;
}
