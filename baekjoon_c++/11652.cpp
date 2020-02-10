#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
    
    int N;
    long long result;
    int count = 1;
    int max = 1;
    long long numbers[1000000];
    
    scanf("%d",&N);
    for (int i = 0; i < N; i++) {
        scanf("%lld",&numbers[i]);
    }
    
    sort(numbers,numbers+N);
    result = numbers[0];
    
    for (int i = 0; i < N; i++) {
        if(numbers[i]==numbers[i+1]) {
            count+=1;
        }
        else{
            count = 1;
        }
        
        if(count > max) {
            max = count;
            result = numbers[i];
        }
    }    
    
    printf("%lld",result);
    
    return 0;
}
