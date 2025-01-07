#include <iostream>
#include <stack>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    queue<int> Q;

    int n; cin >> n;

    while(n>0){
        string text;

        cin >> text;

        if(text == "push"){
            int num; cin >> num;
            Q.push(num);
        }else if(text =="pop"){
            if(!Q.empty()){
                cout<< Q.front()<< "\n";
                Q.pop();
            }else{
                cout << "-1"<< "\n";
            }
        }else if(text == "size"){
            cout << Q.size()<< "\n";
        }else if(text == "empty"){
            if(Q.empty()){
                cout << "1"<< "\n";
            }else{
                cout << "0"<< "\n";
            }
        }else if(text == "front"){
            if(!Q.empty()){
                cout << Q.front()<< "\n";
            }else{
                cout << -1<< "\n";
            }
        }else if(text == "back"){
            if(!Q.empty()){
                cout << Q.back()<< "\n";
            }else{
                cout << -1<< "\n";
            }
        }
        n--;
    }

    return 0;
}
