#include <iostream>
#include <cmath>

using namespace std;

int main(void)
{
    int T;
    double x,y;
    double check,point,distance;
    int count;
    
    scanf("%d",&T);
    
    for (int i = 0; i < T; i++) {
        scanf("%lf %lf", &x, &y);
        
        distance = y-x;
        check = floor(sqrt(distance));
        point = pow(check,2);
        
        if(point==distance){
            count = int(2*check-1);
        } else if(point<distance){
            if(distance-point<=check) {
                count = int(2*check-1)+1;
            } else {
                count = int(2*check-1)+2;
            }
        } else{
            if(point-distance<=check-1) {
                count = int(2*check-1);
            } else {
                count = int(2*check-1)-1;
            }
        }
    
        printf("%d\n", count);
        
    }
    
    
    return 0;
}
