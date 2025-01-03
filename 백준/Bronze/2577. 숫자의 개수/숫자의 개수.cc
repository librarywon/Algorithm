#include <iostream>
#include <vector>
#include <string>
#include <list>
using namespace std;


int main() {
    ios::sync_with_stdio(0),cin.tie(0);

    int sum = 1;
    vector<int> v(10,0);

    for(int i=0;i<3;i++){
        int n;
        cin >> n;
        sum *= n;
    }

    while(sum>0){
        v[sum%10] +=1;
        sum /= 10;
    }

    for(auto n:v) cout << n << "\n";

    return 0;
}
