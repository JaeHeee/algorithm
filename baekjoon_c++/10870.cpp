#include <iostream>

using namespace std;

int fib(int n) {
    if(n==0){
        return 0;
    } else if(n==1) {
        return 1;
    } else {
        return fib(n-1)+ fib(n-2);    
    }
}

int main(void) {
    int n;
    int result;
    
    scanf("%d",&n);
    
    result = fib(n);
    printf("%d",result);
    
    return 0;
}
