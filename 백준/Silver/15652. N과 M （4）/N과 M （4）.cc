#include<iostream>
#include<algorithm>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

int n,m;
int ans[9];

void back_track(int cnt){
    if(cnt == m){
        for(int i=0;i<m;i++){
            cout << ans[i] << " ";
        }
        cout <<"\n";
        return;
    }

    for(int i=1;i<=n;i++){
        if(cnt==0 || (ans[cnt-1] <= i)){
            ans[cnt] = i;
            back_track(cnt+1);
        }
    }
}
int main(){
    fast_io
    cin >> n >> m;
    back_track(0);
}