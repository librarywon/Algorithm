#include<iostream>
#include<algorithm>
#include<numeric>
#include<stack>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

class Data{
public:
    int idx,num,NGE =-1;
};

int n;
vector<int> res(1000001);
stack<Data> s;

int main(){
    fast_io;
    cin >> n;
    for(int i=0;i<n; i++){
        int x; cin >>x;
        while(!s.empty() && s.top().num < x){
            s.top().NGE = x;
            res[s.top().idx] = s.top().NGE;
            s.pop();
        }
        s.push({i,x});
    }
    while (!s.empty()){
        res[s.top().idx]= s.top().NGE;
        s.pop();
    }
    for(int i=0;i<n;i++) cout << res[i] << ' ';

    return 0;
}