#include<iostream>
#include<algorithm>
#include<math.h>
#include <numeric>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

int main(){
    fast_io

    double div =0.0;
    int m,n; cin >> m >> n;
    int sum=0,min=10000+1;

    for(int i=m;i<=n;i++) {
        if(!modf(sqrt(i),&div)){
            sum += i;
            if(min>i){
                min = i;
            }
        }
    }
    if(sum != 0) {
        cout << sum << "\n" << min;
    }else{
        cout << -1;
    }
}