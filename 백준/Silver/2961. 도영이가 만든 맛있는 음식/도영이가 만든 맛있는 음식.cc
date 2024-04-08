#include<iostream>
#include<string>
#include<algorithm>
#include <numeric>
#include <vector>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

vector<int> s1(10),b1(10);
vector<pair<int,int>> ra,rb;
int v[10];
int n;
long long min_diff = 1000000000;

void back_track(int cnt,int mul,int sum){
    if(cnt > 0){ // 적어도 하나의 재료를 사용했을 때
        if(min_diff > abs(mul - sum) )
        min_diff = abs(mul - sum);
    }

    for(int i=0;i<n;i++){
        if(!v[i]){
            v[i]= true;
            back_track(cnt+1,mul * s1[i],sum+b1[i]);
            v[i]= false;
        }
    }
}

int main(){
    fast_io
    cin >> n;

    for(int i=0;i<n;i++){
        int s,b;
        cin >> s >> b;
        s1[i] = s;
        b1[i] = b;
    }
    back_track(0,1,0);
    cout << min_diff;
}