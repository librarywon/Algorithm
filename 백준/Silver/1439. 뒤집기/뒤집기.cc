#include <iostream>
#include <algorithm>
using namespace std;
#define fast_io cin.tie(NULL); ios_base::sync_with_stdio(false);

int main(){
    fast_io
    string s; cin >> s;
    long long cnt=0;

    for (int i = 1; i <s.length(); i++) {
        if(s[i]!=s[i-1]) cnt++;
    }

    if (cnt%2==0) {
        cout<< cnt/2;
    }else {
        cout << (cnt+1)/2;
    }
}