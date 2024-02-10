package chapter3

var timeTable : MutableList<List<Int>> = mutableListOf()
fun main() {

    val n = readln().toInt()

    for (i in 1..n) {
        val m_time = readln().split(" ").map { it.toInt() }
        timeTable.add(m_time)
    }

    val timeTable = timeTable.sortedWith(compareBy({ it[1] }, { it[0] }))

    var end = -1
    var count= 0

    for (time in timeTable) {
        if (end <= time.first()) {
            end = time.last()
            count++
        }
    }

    println(count)
}