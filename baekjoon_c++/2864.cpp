#include <iostream>
#include <string>

using namespace std;

int main()
{
    string a,b;
    int max[2];
    int min[2];
    cin >> a >> b;
    
    for (int i = 0; i < a.size(); i++) {
        if(a[i]=='5'){
            a[i]='6';
        }
    }
    max[0] = atoi(a.c_str());
    
    for (int i = 0; i < a.size(); i++) {
        if(a[i]=='6'){
            a[i]='5';
        }
    }
    min[0] = atoi(a.c_str());
    
    for (int i = 0; i < a.size(); i++) {
        if(b[i]=='5'){
            b[i]='6';
        }
    }
    max[1] = atoi(b.c_str());
    
    for (int i = 0; i < a.size(); i++) {
        if(b[i]=='6'){
            b[i]='5';
        }
    }
    min[1] = atoi(b.c_str());
    
    printf("%d %d",min[0]+min[1],max[0]+max[1]);
    return 0;
}
