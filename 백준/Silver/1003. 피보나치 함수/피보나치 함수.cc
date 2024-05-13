#include<iostream>
#include<string.h>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

int main() {
    fast_io
    int T;
    int num[41][2] = {{1,0},{0,1},};
    cin >> T;
    for(int i=2;i<41;i++){
        num[i][0] = num[i-1][0] + num[i-2][0];
        num[i][1] = num[i-1][1] + num[i-2][1];
    }
    for(int i=0;i<T;i++){
        int k;
        cin >> k;
        cout << num[k][0] << " " << num[k][1] << "\n";
    }

    
    
    
    return 0;
}