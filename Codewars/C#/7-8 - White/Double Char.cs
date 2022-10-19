// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/56b1f01c247c01db92000076
// # Notes  : tag-codewars, tag-kyu-8
// #-----------------------------------------------------------

using System.Collections;

namespace Codewars
{
    public class Kata
    {
        public static string DoubleChar(string s)
        {
            string ss = "";
            foreach (char c in s)
            {
                ss += c;
                ss += c;
            }
            return ss;
        }
    }
}