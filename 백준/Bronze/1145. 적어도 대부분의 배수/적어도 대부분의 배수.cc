#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <numeric>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

int main() {
    fast_io

    int a[5],res = 1000000+1;
    vector<int> v = {0,0,1,1,1};
    for(int i=0;i<5;i++) cin >> a[i];

    do{
        int x=1;

        for(int i=0;i<5;i++) {
            if(v[i]) {
                x = lcm(x,a[i]);
            }
        }
        res = min(res,x);
    } while (next_permutation(v.begin(),v.end()));

    cout << res;


    return 0;
}
