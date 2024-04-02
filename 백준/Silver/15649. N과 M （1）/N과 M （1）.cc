#include<iostream>
#include<algorithm>
#include <numeric>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

int n,m;
int v[9],ans[9];

void back_track(int depth){
    if(depth == m){
        for(int i=0;i<m;i++) {
            cout<< ans[i] << " ";
        }
        cout << "\n";
        return;
    }

    for(int i=1;i<=n;i++){
        if(!v[i]) {
            v[i]= true;
            ans[depth]= i;
            back_track(depth+1);
            v[i] = false;
        }
    }
}

int main(){
    fast_io
    cin >> n >> m;
    back_track(0);
}