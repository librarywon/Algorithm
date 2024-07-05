package boostcamp

import kotlin.Float as Float1

fun calRating(rating: String) : Double {
    return when(rating){
        "A+" -> 4.5
        "A0" -> 4.0
        "B+" -> 3.5
        "B0" -> 3.0
        "C+" -> 2.5
        "C0" -> 2.0
        "D+" -> 1.5
        "D0" -> 1.0
        "F" -> 0.0
        else -> 0.0
    }
}

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()

    var sumRating: Double = 0.0
    var sumNum: Double = 0.0

    repeat(20) {
        val data = br.readLine().split(" ")
        val num = data[1].toDouble()
        val rating = data[2]

        if (rating != "P") {
            sumRating += num
            sumNum += calRating(rating) * num
        }
    }

    bw.write("%.6f".format(sumNum/sumRating))
    bw.flush()
    bw.close()
}