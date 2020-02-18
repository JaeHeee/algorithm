#include <iostream>

using namespace std;

int main(void){
    int day;
    int number;
    int count=0;
    
    scanf("%d",&day);
    
    for (int i = 0; i < 5; i++) {
        scanf("%d",&number);
        if(number == day){
            count++;
        }
    }
    
    printf("%d",count);
    
    return 0;
}
