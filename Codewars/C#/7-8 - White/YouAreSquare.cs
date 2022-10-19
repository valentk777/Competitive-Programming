// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/54c27a33fb7da0db0100040e
// # Notes  : tag-codewars, tag-kyu-7
// #-----------------------------------------------------------

using System.Collections;

namespace Codewars
{
    public class Kata
    {
        public static bool IsSquare(int n)
        {
            return Math.Sqrt(n) % 1 == 0;
        }
    }
}