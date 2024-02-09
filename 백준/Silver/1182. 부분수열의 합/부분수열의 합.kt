package chapter2

val firstLine = readln().split(" ").map { it.toInt() }
val numberSize = firstLine[0]
val input_sum = firstLine[1]

val numbers  = readln().split(" ").map { it.toInt() }

var count = 0

fun dfs(index : Int, currentSum : Int)  {

    if (index >= numberSize) {
        return
    }

    val newSum = currentSum + numbers[index]

    if (currentSum + numbers[index] == input_sum) {
        count++
    }

    dfs(index+1,newSum)
    dfs(index+1,currentSum)
}

fun main(args: Array<String>) {

    dfs(0,0)

    println(count)
}