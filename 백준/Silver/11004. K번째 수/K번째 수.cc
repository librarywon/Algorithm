#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define fast_io cin.tie(NULL); ios_base::sync_with_stdio(false);

int main()
{
    fast_io
    int n,k; cin >> n >> k;
    vector<int> num(n);

    for(int i =0;i<n;i++) {
        int a; cin >> a;
        num[i] = a;
    }

    sort(num.begin(),num.end());
    cout << num[k-1];
    return 0;
}