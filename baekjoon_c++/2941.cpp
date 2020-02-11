#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    string str;
    string c;
    int length=0;
    bool check = true;
    vector<pair<string, int>> ca;
    
    ca.push_back(pair<string, int>("c=",2));
    ca.push_back(pair<string, int>("c-",2));
    ca.push_back(pair<string, int>("dz=",3));
    ca.push_back(pair<string, int>("d-",2));
    ca.push_back(pair<string, int>("lj",2));
    ca.push_back(pair<string, int>("nj",2));
    ca.push_back(pair<string, int>("s=",2));
    ca.push_back(pair<string, int>("z=",2));
    
    cin >> str;
    
    while(check) {
        check = false;
        for (int i = 0; i < ca.size(); i++) {
            if(str.find(ca[i].first) != string::npos) {
                if(i==7 && (str.find(ca[2].first) != string::npos)) {
                    str.replace(str.find(ca[2].first),ca[2].second,".");
                    length++;
                    check = true;
                    continue;
                }
                str.replace(str.find(ca[i].first),ca[i].second,".");
                length++;
                check = true;
            }
        }
    }
    
    for (int i = 0; i < str.size(); i++) {
        c = str[i];
        if(c.compare(".") && c.compare("=") && c.compare("-")) {
            length+=1;
        }
    }
    
    printf("%d",length);
    
    return 0;
}
