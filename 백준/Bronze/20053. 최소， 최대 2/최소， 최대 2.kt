package boostcamp

import kotlin.math.max

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()

    val n = br.readLine().toInt()

    repeat(n){
        val cnt = br.readLine()
        val nums = br.readLine().split(" ").map { it.toInt() }.toIntArray()
        bw.write("${nums.min()} ${nums.max()}")
        bw.newLine()
    }
    bw.flush()
    bw.close()
}