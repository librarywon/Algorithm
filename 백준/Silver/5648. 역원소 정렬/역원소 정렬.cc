#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
#define fast_io cin.tie(NULL); ios_base::sync_with_stdio(false);

int main() {
    fast_io
    long long n; cin >> n;
    vector<long long> num(n);

    for(int i=0;i<n;i++) {
        string s; cin >> s;
        reverse(s.begin(),s.end());
        num[i] = stoll(s);
    }
    sort(num.begin(),num.end());

    for(int i=0;i<n;i++){
        cout << num[i] << "\n";
    }

    return 0;
}
