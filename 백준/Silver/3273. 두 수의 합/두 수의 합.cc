#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0),cin.tie(0);

    vector<int> v(2000001,0);
    vector<int> vv;

    int n; cin >> n;

    for(int i=0;i<n;i++){
        int num; cin >> num;
        vv.push_back(num);
        v[num] = 1;
    }
    int a; cin >> a;
    int answer = 0;

    for(auto k:vv){
        if(k > a) continue;
        if(v[abs(a-k)]){
            answer +=1;
        }
    }
    cout << answer/2;

    return 0;
}
