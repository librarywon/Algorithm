#include<iostream>
#include<algorithm>
#include <numeric>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

int main(){
    fast_io

    while(1){
        int n; cin >> n;
        if(n==0){
            return 0;
        }

        vector<int> a(n);
        for(int i=0;i<n;i++) cin >> a[i];

        vector<int> comb(n, 0);
        fill(comb.begin(), comb.begin() + 6, 1);

        do {
            for(int i=0;i<n;i++){
                if(comb[i]){
                    cout << a[i] <<" ";
                }
            }
            cout << "\n";
        }while(prev_permutation(comb.begin(),comb.end()));
        cout << "\n";
    }
}