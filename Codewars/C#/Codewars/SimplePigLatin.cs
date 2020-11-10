// #-----------------------------------------------------------
// #
// # https://www.codewars.com/kata/520b9d2ad5c005041100000f
// #
// #-----------------------------------------------------------

namespace Codewars
{
    public class SimplePigLatin
    {
        public static string PigIt(string str)
        {
            var listStr = str.Split(" ");
            var newStr = "";

            foreach (var s in listStr)
                newStr += $"{(s + s[0])[1..]}ay ";

            return newStr.Remove(newStr.Length - 1);
        }
    }
}