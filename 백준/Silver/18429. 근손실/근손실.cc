#include<iostream>
#include<string>
#include<algorithm>
#include <numeric>
#include <vector>
using namespace std;

#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

int cnt=0,n,k;
int w[51];
int v[51];

void back_track(int day,int sum){
    if(sum <500){
        return;
    }

    if(day==n){
        cnt++;
        return;
    }

    for(int i=0;i<n;i++){
        if(!v[i]){
            v[i] = true;
            back_track(day+1,sum + w[i] - k);
            v[i] = false;
        }
    }
}

int main(){
    fast_io

    cin >> n >> k;
    for(int i =0;i<n;i++) cin >> w[i];
    back_track(0,500);
    cout << cnt;
}