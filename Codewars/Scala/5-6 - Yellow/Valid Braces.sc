/** -----------------------------------------------------------
 * URL    : https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/scala
 * Notes  : tag-codewars, tag-kyu-6
 * ----------------------------------------------------------- */

def validBraces(s: String): Boolean = {
  @scala.annotation.tailrec
  def filterBrackets(c: Int, n: String): Boolean = {
    val newString = n.replace("()", "")
      .replace("[]", "")
      .replace("{}", "")

    if (newString.length == 0) true
    else if (newString.length == c) false
    else filterBrackets(newString.length, newString)
  }

  filterBrackets(s.length, s)
}


validBraces("([{}])")
validBraces("[({})](]")