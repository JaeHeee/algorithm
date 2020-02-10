#include <iostream>

using namespace std;

int even[500001], odd[500001];

int main()
{
    int N,H;
    int evenMax = 0;
    int oddMax = 0;
    int min = 200001;
    int positions=0;
    
    scanf("%d %d",&N,&H);
    for (int i = 0; i < N/2; i++) {
        int e,o;
        scanf("%d %d",&e,&o);
        even[e]++;
        odd[o]++;
        if(evenMax < e) {
            evenMax = e;
        }
        if(oddMax < o) {
            oddMax = o;
        }
    }
    
    for (int i = evenMax; i >= 1; i--) {
        even[i] += even[i+1];
    }
    for (int i = oddMax; i >= 1; i--) {
        odd[i] += odd[i+1];
    }
    
    for (int i = 1; i <= H; i++) {
        if(even[i]+odd[H-i+1]<min) {
            positions = 1;
            min = even[i]+odd[H-i+1];
        } else if(even[i]+odd[H-i+1] == min) {
            positions++;
        }
    }
    
    printf("%d %d\n",min,positions);
    
    
    return 0;
}
