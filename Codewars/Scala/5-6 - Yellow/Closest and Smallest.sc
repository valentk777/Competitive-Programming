/** -----------------------------------------------------------
 * URL    : https://www.codewars.com/kata/5868b2de442e3fb2bb000119
 * Notes  : tag-codewars, tag-kyu-5
 * ----------------------------------------------------------- */

def closest(strng: String): Array[(Int, Int, Int)] = {
  strng.split(" ") match {
    case numbers if numbers.size < 2 =>
      Array()
    case numbers =>
      val weightsAndPositions = numbers
        .zipWithIndex
        .map { case (element, index) => (element.map(_.asDigit).sum, index, element.toInt) }
        .sortBy(x => x._1)

      val result = weightsAndPositions.zip(weightsAndPositions.drop(1))
        .map({ case (first, second) => (first, second, second._1 - first._1) })
        .minBy(x => x._3)

      Array(result._1, result._2)
  }
}

closest("456899 50 11992 176 272293 163 389128 96 290193 85 52") sameElements Array((13, 9, 85), (14, 3, 176))
closest("239382 162 254765 182 485944 134 468751 62 49780 108 54") sameElements Array((8, 5, 134), (8, 7, 62))
closest("241259 154 155206 194 180502 147 300751 200 406683 37 57") sameElements Array((10, 1, 154), (10, 9, 37))
closest("89998 187 126159 175 338292 89 39962 145 394230 167 1") sameElements Array((13, 3, 175), (14, 9, 167))
closest("462835 148 467467 128 183193 139 220167 116 263183 41 52") sameElements Array((13, 1, 148), (13, 5, 139))
closest("403749 18 278325 97 304194 119 58359 165 144403 128 38") sameElements Array((11, 5, 119), (11, 9, 128))
closest("28706 196 419018 130 49183 124 421208 174 404307 60 24") sameElements Array((6, 9, 60), (6, 10, 24))
closest("189437 110 263080 175 55764 13 257647 53 486111 27 66") sameElements Array((8, 7, 53), (9, 9, 27))
closest("79257 160 44641 146 386224 147 313622 117 259947 155 58") sameElements Array((11, 3, 146), (11, 9, 155))
closest("315411 165 53195 87 318638 107 416122 121 375312 193 59") sameElements Array((15, 0, 315411), (15, 3, 87))
