#include <iostream>
#include <vector>
#include <string>
#include <list>
using namespace std;

list<char> L;

int main() {
    ios::sync_with_stdio(0),cin.tie(0);
    string a;
    cin >> a;

    for(auto i : a) L.push_back(i);
    auto l = L.end();

    int n ;
    cin >> n;
    for(int i=0;i<n;i++){
        char input;
        cin >> input;

        if(input == 'L'){
            if(l != L.begin()) l--;
        }
        else if(input == 'D'){
            if(l != L.end()) l++;
        }
        else if(input == 'B'){
            if(l != L.begin()) {
                l--;
                l = L.erase(l);
            }
        }
        else if(input == 'P') {
            char p_char;
            cin >> p_char;
            L.insert(l, p_char);
        }
    }

    for(auto c: L){
        cout << c;
    }

    return 0;
}
