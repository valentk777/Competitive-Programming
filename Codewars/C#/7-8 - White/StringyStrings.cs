// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/563b74ddd19a3ad462000054
// # Notes  : tag-codewars, tag-kyu-8
// #-----------------------------------------------------------

namespace Codewars
{
    public class Kata
    {
        public static string Stringy(int size)
        {
            var r = "";
            for (int i = 0; i < size; i++)
                r += i % 2 == 0 ? "1" : "0";
            return r;
        }
    }
}