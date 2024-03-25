#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);
typedef long long ll;

ll length(ll a,ll b){
    return abs(b-a);
}

int main(){
    fast_io
    ll n,sum=0; cin >> n;
    vector<pair<ll, ll> > num;

    for(int i = 0; i < n; i++){
        ll x, y;
        cin >> x >> y;
        num.push_back(make_pair(x,y));
    }
    sort(num.begin(), num.end());

    ll R,S=0;
    R= num[0].first;
    S= num[0].second;
    sum += length(R,S);
    for(int i =1;i<n;i++){
        ll x = num[i].first;
        ll y = num[i].second;
        if(S < x){
            sum += length(x,y);
            R=x;
            S=y;
        }else if(S <y) {
            sum += length(S, y);
            S = y;
        }
    }

    cout << sum;

    return 0;
}
