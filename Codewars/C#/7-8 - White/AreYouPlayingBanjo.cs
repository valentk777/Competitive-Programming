// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/53af2b8861023f1d88000832
// # Notes  : tag-codewars, tag-kyu-8
// #-----------------------------------------------------------

using System;

namespace Codewars
{

    public class Kata
    {
        public static string AreYouPlayingBanjo(string name) =>
          name + (name.ToUpper()[0] == 'R' ? " plays banjo" : " does not play banjo");
    }
}