#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main() {
    ios::sync_with_stdio(0),cin.tie(0);
    string a;
    cin >> a;

    vector<int> v(26,0);

    for(char c: a){
        v[c-'a'] +=1;
    }

    for(int q: v) cout << q <<" ";
    return 0;
}
