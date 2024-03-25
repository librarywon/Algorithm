#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;
#define fast_io cin.tie(NULL);ios_base::sync_with_stdio(false);

void bfs() {
    int F, S, G, U ,D;
    cin >> F >> S >> G >> U >> D;

    vector<bool> visited(F+1,false);
    queue<int> q;
    int elv[2]= {U,-D};

    q.push(S);
    visited[S] = true;

    int level =0;

    while(!q.empty()){
        int qSize = q.size();
        for(int i=0; i<qSize;i++) {
            int curr = q.front();
            if(curr == G) {
                cout << level;
                return;
            }
            q.pop();
            for(int go: elv){
                if(curr+go >0 && curr+go<=F && !visited[curr+go]) {
                    visited[curr+go] = true;
                    q.push(curr+go);
                }
            }
        }
        level++;
    }
    cout << "use the stairs";
}

int main(){
    fast_io

    bfs();
    return 0;
}