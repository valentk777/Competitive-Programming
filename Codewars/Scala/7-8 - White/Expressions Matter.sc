/** -----------------------------------------------------------
 * URL    : https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
 * Notes  : tag-codewars, tag-kyu-8
 * ----------------------------------------------------------- */

def expressionMatter(a: Int, b: Int, c: Int): Int =
  List(
    a + b + c,
    a * b + c,
    a + b * c,
    a * (b + c),
    (a + b) * c,
    a * b * c).max


expressionMatter(3, 5, 7)