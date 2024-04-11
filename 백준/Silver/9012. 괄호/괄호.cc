#include<iostream>
#include<algorithm>
#include<numeric>
#include<stack>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

void check_vps(string s){
    stack<int>st;

    for(int k : s){
        if(k =='('){
            st.push(1);
        }else if(k == ')'){
            if(st.empty()){
                cout << "NO" << endl;
                return;
            }else{
                st.pop();
            }
        }
    }
    if(st.empty()){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
}

int main(){
    fast_io
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        string s;
        cin >> s;
        check_vps(s);
    }
    return 0;
}