#include <iostream>
#include <algorithm>
using namespace std;
#define fast_io cin.tie(NULL); ios_base::sync_with_stdio(false);

int main(){
    fast_io
    string n; cin >> n;
    bool flag = true;
    long long sum =0;

    if(n.length()==1) {
        cout << "-1";
        return 0;
    }

    for (int i = 0; i <n.length() ; ++i) {
        sum += n[i] - '0' ;
        if(n[i]=='0'){
            flag =false;
        }
    }

    if (flag) {
        cout << "-1";
        return 0;
    }

    if(sum%3==0) {
        sort(n.rbegin(), n.rend());
        cout << n;
    }else {
        cout << "-1";
    }

    return 0;
}
