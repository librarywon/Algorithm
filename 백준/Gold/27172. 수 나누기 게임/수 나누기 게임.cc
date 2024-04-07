#include<iostream>
#include<string>
#include<algorithm>
#include <numeric>
#include <vector>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

int main(){
    fast_io

    int n,max=1000002;
    cin >> n;
    vector<int> a(n);
    vector<int> r(max,max);

    for(int i=0;i<n;i++) {
        int in; cin >> in;
        a[i] = in;
        r[in] = 0;
    }

    for(int i=0;i<n;i++) {
        for(int j=a[i]*2;j<max;j+=a[i]){
            if(max == r[j]) continue;
            r[j] += -1;
            r[a[i]] += 1;
        }
    }

    for(int i=0;i<n;i++){
        cout << r[a[i]] << " ";
    }

}