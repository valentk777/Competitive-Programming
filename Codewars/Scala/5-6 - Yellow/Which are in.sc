/** -----------------------------------------------------------
 * URL    : https://www.codewars.com/kata/550554fd08b86f84fe000a58
 * Notes  : tag-codewars, tag-kyu-6
 * ----------------------------------------------------------- */

object WhichAreIn {

  def inArray(array1: Array[String], array2: Array[String]): Array[String] = {
    var r = Set[String]()
    for (element <- array1) {
      if (array2.exists(_ contains element)) {
        r += element
      }
    }
    return r.toArray.sorted
  }
}