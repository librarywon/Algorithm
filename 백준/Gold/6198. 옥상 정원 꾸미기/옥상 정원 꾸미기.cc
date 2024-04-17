#include <iostream>
#include <stack>
using namespace std;

int main() {
    int n;
    cin >> n;
    stack<int> heights;
    long long visibleCount = 0;

    for (int i = 0; i < n; i++) {
        int h;
        cin >> h;
        while (!heights.empty() && heights.top() <= h) {
            heights.pop();
        }
        visibleCount += heights.size();
        heights.push(h);
    }

    cout << visibleCount;
    return 0;
}