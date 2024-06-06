class Solution {
   fun solution(k: Int, tangerine: IntArray): Int {
    var answer = 0
    val d = mutableMapOf<Int, Int>()
    
    // 딕셔너리에 있다면 +1, 없다면 {"s":1} 생성
    for (s in tangerine) {
        d[s] = d.getOrDefault(s, 0) + 1
    }
    
    // 크기별 개수를 더해서 k랑 비교할 변수
    var sl = 0
    // 정렬된 귤 크기별 갯수 기준으로 내림차순 리스트
    val sortedValues = d.values.sortedDescending()
    for (c in sortedValues) {
        if (sl >= k) {
            break
        }
        sl += c
        answer += 1
    }
    
    return answer
}

}