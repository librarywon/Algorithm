#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> v(n); // 입력 수열
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    stack<int> s;
    vector<char> operations;

    int current = 1; // 현재 스택에 push할 숫자
    for (int num : v) {
        // 스택이 비어있거나, 스택의 top이 원하는 숫자가 아닐 경우 push
        while (s.empty() || s.top() < num) {
            if (current > n) break; // 범위 초과 시 종료
            s.push(current++);
            operations.push_back('+');
        }

        // 원하는 숫자가 스택의 top에 있으면 pop
        if (!s.empty() && s.top() == num) {
            s.pop();
            operations.push_back('-');
        } else {
            // 원하는 숫자를 만들 수 없을 경우
            cout << "NO\n";
            return 0;
        }
    }

    // 모든 연산 출력
    for (char op : operations) {
        cout << op << '\n';
    }

    return 0;
}
