#include<iostream>
#include<string>
#include<algorithm>
#include <numeric>
#include <vector>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

int main(){
    fast_io
    unsigned int a,b;
    cin >> a >> b;

    cout << (a ^ b);
}