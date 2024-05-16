#include <string>
#include <vector>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    
    for(int i=0;i<n;i++){
        int n_or = arr1[i]|arr2[i];
        string s;
        
        for(int j=0;j<n;j++){
            if(n_or%2 == 0){
                s = " "+ s;
            }else{
                s = "#" + s ;
            }
            n_or = n_or/2;
        }
        answer.push_back(s);
    }
    
    return answer;
}