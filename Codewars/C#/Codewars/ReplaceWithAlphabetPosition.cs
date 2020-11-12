// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/59c01248bf10a47bd1000046
// # Notes  : tag-codewars
// #-----------------------------------------------------------

using System.Linq;
using System.Text;

namespace Codewars
{
    public class ReplaceWithAlphabetPosition
    {
        public static string AlphabetPosition(string text) =>
            string.Join(" ", Encoding.ASCII.GetBytes(text).Where(s => ((s > 64) && (s < 91)) || ((s > 96) && (s < 123))).Select(s => (s > 64) && (s < 91) ? s - 64 : s - 96));
    }
}