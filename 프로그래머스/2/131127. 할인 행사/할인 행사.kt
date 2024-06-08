class Solution {
    fun solution(want: Array<String>, number: IntArray, discount: Array<String>): Int {
    // 원하는 제품과 수량을 맵으로 초기화
    val wantMap = want.indices.associate { want[it] to number[it] }
    
    val windowSize = 10
    val discountLength = discount.size
    var answer = 0

    // 첫 번째 10일 윈도우 초기화
    val currentWindow = discount.take(windowSize).groupingBy { it }.eachCount().toMutableMap()

    // 초기 윈도우가 원하는 제품 조건을 만족하는지 확인
    if (wantMap.all { (item, qty) -> currentWindow.getOrDefault(item, 0) >= qty }) {
        answer += 1
    }

    // 슬라이딩 윈도우를 사용하여 할인 배열을 검사
    for (i in windowSize until discountLength) {
        // 윈도우에서 빠지는 요소 개수 감소
        val outItem = discount[i - windowSize]
        currentWindow[outItem] = currentWindow.getOrDefault(outItem, 0) - 1
        if (currentWindow[outItem]!! <= 0) {
            currentWindow.remove(outItem)
        }

        // 윈도우에 새로 들어오는 요소 개수 증가
        val inItem = discount[i]
        currentWindow[inItem] = currentWindow.getOrDefault(inItem, 0) + 1

        // 현재 윈도우가 원하는 제품 조건을 만족하는지 확인
        if (wantMap.all { (item, qty) -> currentWindow.getOrDefault(item, 0) >= qty }) {
            answer += 1
        }
    }

    return answer
}
}

