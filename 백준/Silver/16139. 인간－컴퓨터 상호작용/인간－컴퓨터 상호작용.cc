#include<iostream>
#include<algorithm>
#include<numeric>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

int main(){
    fast_io

    string s;
    int q;
    cin >> s;
    cin >> q;
    long long sSize = s.size();
    long long pSum[27][s.size()+1];

    for(int i=0;i<'z'-'a'+1;i++){
        for (int (j) = 1; (j) <sSize+1 ;j++) {
            if(s[j-1]-'a'==i){
                pSum[i][j] = pSum[i][j-1] +1;
            }else{
                pSum[i][j] = pSum[i][j-1];
            }
        }
    }


    for(int i=0;i<q;i++){
        char c;
        int l,r,k;
        cin >> c >> l >> r;

        cout<< pSum[c-'a'][r+1] - pSum[c-'a'][l] << "\n";
    }
    return 0;
}