#include <iostream>
#include <algorithm>

using namespace std;

int N;
int S=0;
int A[50];
int B[50];

bool compare(int a,int b){
        return a>b;
    }

int main()
{
    scanf("%d",&N);
    for (int i = 0; i < N; i++) {
        scanf("%d",&A[i]);
    }
    for (int i = 0; i < N; i++) {
        scanf("%d",&B[i]);
    }
    
    
    
    sort(A,A+N);
    sort(B,B+N,compare);
    
    for (int i = 0; i < N; i++) {
        S += A[i]*B[i];
    }
    
    printf("%d",S);
    return 0;
}
