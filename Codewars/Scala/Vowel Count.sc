/** -----------------------------------------------------------
 * URL    : https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/scala
 * Notes  : tag-codewars
 * ----------------------------------------------------------- */

val vowels = List('a', 'e', 'i', 'o', 'u')

def getCount(inputStr: String): Int = inputStr.filter(vowels.contains).length

getCount("absbsbsbaa")