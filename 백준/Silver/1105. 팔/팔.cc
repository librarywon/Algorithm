#include <iostream>
#include <string>
using namespace std;
#define fast_io cin_tie(NULL);ios_base::sync_with_stdio(false);

int main() {
    string L, R;
    cin >> L >> R;
    long long sum = 0;

    if(L.length() != R.length()) {
        cout << "0";
        return 0;
    }
    else{
        for (int i = 0; i < L.length(); i++) {
            if(L[i] != R[i]) {
                cout << sum;
                return 0;
            }else {
                if(L[i] == '8') {
                    sum++;
                }
            }
        }
    }
    cout << sum;

    return 0;
}
