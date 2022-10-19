// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/53dc23c68a0c93699800041d
// # Notes  : tag-codewars, tag-kyu-8
// #-----------------------------------------------------------

namespace Codewars
{
    public class Kata
    {
        public static string Smash(string[] words)
        {
            string naujasZodis = "";

            foreach (string zodis in words)
            {
                naujasZodis += zodis + " ";
            }

            return naujasZodis.Trim();
        }
    }
}