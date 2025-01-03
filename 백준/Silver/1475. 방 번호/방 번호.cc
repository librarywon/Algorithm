#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;


int main() {
    ios::sync_with_stdio(0),cin.tie(0);

    int n; cin >> n;
    vector<int> v(10,0);

    while(n>0){
        v[n%10] += 1;
        n /= 10;
    }
    int max_n = 0;
    for(int i=0;i<10;i++){
        if(i == 9){
            continue;
        }
        
        if(i == 6){
            max_n = max(max_n,int(ceil((v[i]+v[9])/2.0)));
        }
        else{
            max_n = max(max_n,v[i]);
        }
    }

    cout << max_n;
    return 0;
}
