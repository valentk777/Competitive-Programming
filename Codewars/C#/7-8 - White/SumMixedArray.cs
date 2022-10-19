// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/57eaeb9578748ff92a000009
// # Notes  : tag-codewars, tag-kyu-8
// #-----------------------------------------------------------

namespace Codewars
{
    public class Kata
    {
        public static int SumMix(object[] x)
        {
            var suma = 0;
            foreach (var e in x)
                suma += int.Parse(e.ToString());
            return suma;
        }
    }
}