#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <math.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0),cin.tie(0);


    int n; cin >>n;

    for(int i=0;i<n;i++){
        list<char> l;
        auto ll = l.begin();

        string s; cin >> s;

        for(auto ss:s){
            if(ss =='<'){
                if(ll != l.begin()){
                    ll--;
                }
            }else if(ss == '>'){
                if(ll != l.end()){
                    ll++;
                }
            }else if(ss == '-'){
                if(ll != l.begin()){
                    ll--;
                    ll = l.erase(ll);
                }
            }else{
                l.insert(ll,ss);
            }
        }

        for(auto sa: l) cout << sa;
        cout << "\n";
    }


    return 0;
}
