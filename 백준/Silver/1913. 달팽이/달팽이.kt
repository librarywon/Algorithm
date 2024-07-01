package boostcamp

fun main(){
    val br = System.`in`.bufferedReader()
    val n = br.readLine().toInt()
    val find = br.readLine().toInt()

    val matrix = Array(n) { IntArray(n) }

    var num = n * n
    var x = 0
    var y = 0
    var dx = arrayOf(1, 0, -1, 0)
    var dy = arrayOf(0, 1, 0, -1)
    var dir = 0
    var findX = 0
    var findY = 0

    while (num > 0) {
        matrix[x][y] = num
        if (num == find){
            findX = x+1
            findY = y+1
        }
        num--
        var nx = x + dx[dir]
        var ny = y + dy[dir]
        if (nx < 0 || nx >= n || ny < 0 || ny >= n || matrix[nx][ny] != 0) {
            dir = (dir + 1) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]
        }
        x = nx
        y = ny
    }

    for (row in matrix) {
        println(row.joinToString(" "))
    }
    println("$findX $findY")
}