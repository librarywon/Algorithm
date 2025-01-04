#include <iostream>
#include <list>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, K;
    cin >> N >> K;

    list<int> l;
    for (int i = 1; i <= N; i++) {
        l.push_back(i);
    }

    auto ll = l.begin();
    cout << "<";

    while (!l.empty()) {
        // K-1번 이동 (K번째에서 삭제)
        for (int i = 0; i < K - 1; i++) {
            ll++;
            if (ll == l.end()) ll = l.begin(); // 끝에 도달하면 처음으로 이동
        }

        // 현재 원소 출력
        if (l.size() > 1)
            cout << *ll << ", ";
        else
            cout << *ll << ">";

        // 원소 삭제 및 반복자 갱신
        ll = l.erase(ll);
        if (ll == l.end()) ll = l.begin(); // 삭제 후 끝이면 처음으로 이동
    }

    return 0;
}
