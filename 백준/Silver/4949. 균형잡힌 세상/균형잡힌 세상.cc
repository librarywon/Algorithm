#include <iostream>
#include <stack>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    getline(cin,s);

    while(s != "."){
        int flag = 1;
        stack<char> st;
        for(auto text: s){
            if(text=='['){
                st.push(text);
            }else if(text == ']'){
                if(!st.empty() && st.top() == '['){
                    st.pop();
                }
                else{
                    flag = 0;
                    break;
                }
            }else if(text == '('){
                st.push(text);
            }else if(text == ')'){
                if(!st.empty() &&st.top() == '('){
                    st.pop();
                }
                else{
                    flag = 0;
                    break;
                }
            }
        }

        if(flag && st.empty()){
            cout << "yes";
        }else{
            cout << "no";
        }
        cout << "\n";
        getline(cin,s);
    }
}
