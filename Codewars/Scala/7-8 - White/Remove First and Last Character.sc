/** -----------------------------------------------------------
 * URL    : https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
 * Notes  : tag-codewars, tag-kyu-8
 * ----------------------------------------------------------- */

object RemoveFirstAndLastCharacters {
  def removeChars(s: String): String = s.drop(1).dropRight(1)
}