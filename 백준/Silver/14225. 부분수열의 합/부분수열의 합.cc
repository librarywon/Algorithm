#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
 * 문제의 핵심은 "수열의 원소를 정렬한 후, 
 * 각 원소를 순서대로 더해가면서 만들 수 있는 합의 범위를 확장해 나가는 것"입니다. 
 * 만약 현재까지의 합이 x이고, 다음 순서의 원소가 y일 때, x + 1 < y라면,
 * x + 1은 만들 수 없는 가장 작은 자연수가 됩니다. 
 * 왜냐하면, 현재까지의 합으로 x까지의 수는 모두 만들 수 있지만, 
 * x + 1을 만들기 위해서는 최소한 x + 1의 값을 가진 원소가 필요하기 때문입니다.
 */

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    // 수열을 오름차순으로 정렬합니다.
    sort(a.begin(), a.end());

    // 만들 수 있는 합의 최대값을 0으로 초기화합니다.
    int maxSum = 0;
    for (int i = 0; i < n; i++) {
        // 현재까지의 합 + 1이 다음 원소보다 작으면, 그 값은 만들 수 없습니다.
        if (maxSum + 1 < a[i]) {
            break;
        }
        maxSum += a[i];
    }

    // 만들 수 없는 가장 작은 자연수는 현재까지의 합 + 1입니다.
    cout << maxSum + 1 << '\n';

    return 0;
}
