#include <iostream>
#include <stack>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    queue<int> Q;

    int n; cin >> n;

    while(n--){
        string t; cin >>t;

        if(t == "push"){
            int nn; cin >> nn;
            Q.push(nn);
        }else if(t == "pop"){
            if(!Q.empty()){
                cout<< Q.front() << "\n";
                Q.pop();
            }else{
                cout << -1 << "\n";
            }
        }else if(t == "size") {
            cout << Q.size() << "\n";
        }else if(t == "empty") {
            if(Q.empty()){
                cout << 1 <<"\n";
            }else{
                cout << 0 << "\n";
            }
        }else if(t == "front"){
            if(!Q.empty()){
                cout<< Q.front() << "\n";
            }else{
                cout << -1 << "\n";
            }
        }else if(t == "back"){
            if(!Q.empty()){
                cout<< Q.back() << "\n";
            }else{
                cout << -1 << "\n";
            }
        }
    }

    return 0;
}
