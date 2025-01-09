#include <iostream>
#include <stack>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    int cnt=0;

    while(n--){
        string s; cin >> s;
        stack<char> st;
        st.push(s[0]);
        for(int i=1;i<s.size();i++){
            if(st.empty()){
                st.push(s[i]);
            }
            else if(st.top() == s[i]){
                st.pop();
            }else{
                st.push(s[i]);
            }
        }

        if(st.empty()){
            cnt++;
        }
    }
    cout << cnt;

}
