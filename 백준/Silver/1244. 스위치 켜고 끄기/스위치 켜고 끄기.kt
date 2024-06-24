package boostcamp

import java.util.*

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()

    val n = br.readLine().toInt()
    val switches = br.readLine().split(" ").map { it.toInt() }.toMutableList()
    val m = br.readLine().toInt()

    repeat(m) {
        val command = br.readLine().split(" ").map { it.toInt() }
        val type = command[0]
        val num = command[1]

        if (type == 1) {
            for (i in num - 1 until n step num) {
                switches[i] = switches[i].inv() and 1
            }
        } else {
            var left = num - 2
            var right = num
            while (left >= 0 && right < n && switches[left] == switches[right]) {
                left--
                right++
            }
            for (i in left + 1 until right) {
                switches[i] = switches[i].inv() and 1
            }
        }
    }

    switches.forEachIndexed { index, state ->
        bw.write("$state ")
        if ((index + 1) % 20 == 0) {
            bw.write("\n")
        }
    }
    bw.write("\n")
    bw.flush()
    bw.close()
    br.close()
}
