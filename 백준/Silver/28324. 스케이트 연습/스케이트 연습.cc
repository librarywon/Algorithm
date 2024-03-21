#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

typedef long long  ll;

int main(){
    fast_io
    int n; cin >> n;
    vector<ll> num(n);
    ll sum=1,k=1;

    for(int i=0;i<n;i++){
        ll limit; cin >> limit;
        num[i] = limit;
    }

    for(int i = n-2 ; i>=0;i--){
        if(k+1 > num[i]) {
            k = num[i];
            sum += num[i];
        }
        else {
            sum += ++k;
        }
    }

    cout << sum;
}
