#include<iostream>
#include<algorithm>
#include <numeric>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

int n,m;
vector<int> nums(10,10000+1);
int a[9],v[9];

void back_track(int cnt){

    if(cnt == m){
        for(int i=0;i<m;i++){
            cout << a[i] << " ";
        }
        cout << "\n";
        return;
    }

    int temp =0;

    for(int i=0;i<n;i++){
        if(!v[i] && nums[i]!=temp &&(cnt==0||a[cnt-1]<=nums[i]) ){
            v[i] =true;
            a[cnt] = nums[i];
            temp = a[cnt];
            back_track(cnt+1);
            v[i] = false;
        }
    }
}

int main(){
    fast_io
    cin >> n >> m;
    for(int i=0;i<n;i++)cin >> nums[i];
    sort(nums.begin(),nums.end());
    back_track(0);
}