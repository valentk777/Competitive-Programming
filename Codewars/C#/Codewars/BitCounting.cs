// #-----------------------------------------------------------
// #
// # https://www.codewars.com/kata/526571aae218b8ee490006f4
// #
// #-----------------------------------------------------------

using System;
using System.Linq;

namespace Codewars
{
    public class BitCounting
    {
        public static int CountBits(int n) => Convert.ToString(n, 2).Where(x => x == '1').Count();
    }
}