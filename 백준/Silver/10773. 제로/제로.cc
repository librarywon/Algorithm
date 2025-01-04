#include <iostream>
#include <stack>
#include <math.h>
#include <numeric>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> s;
    int n;
    cin >> n;

    for(int i=0;i<n;i++){
        int nn; cin >> nn;

        if(nn == 0){
            s.pop();
        }else {
            s.push(nn);
        }
    }
    int sum =0;
    while(!s.empty()){
        sum += s.top();
        s.pop();
    }
    
    cout << sum;

    return 0;
}
