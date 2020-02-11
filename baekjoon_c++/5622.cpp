#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    string str;
    int t = 0;
    vector<pair<string, int> > tel;
    
    tel.push_back(pair<string, int>("ABC",3));
    tel.push_back(pair<string, int>("DEF",4));
    tel.push_back(pair<string, int>("GHI",5));
    tel.push_back(pair<string, int>("JKL",6));
    tel.push_back(pair<string, int>("MNO",7));
    tel.push_back(pair<string, int>("PQRS",8));
    tel.push_back(pair<string, int>("TUV",9));
    tel.push_back(pair<string, int>("WXYZ",10));
    
    cin >> str;
    
    for (int i = 0; i < str.size(); i++) {
        for (int j = 0; j < tel.size(); j++) {
            if((tel[j].first).find(str[i])!=string::npos) {
                t += tel[j].second;
            }
        }
    }
    
    printf("%d",t);
    
    return 0;
}
