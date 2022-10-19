// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/59f7a0a77eb74bf96b00006a
// # Notes  : tag-codewars, tag-kyu-7
// #-----------------------------------------------------------

using System;

namespace Codewars
{
    public static class Kata
    {
        public static int GolfScoreCalculator(string par, string score)
        {
            var suma = 0;
            Console.WriteLine(par);
            Console.WriteLine(score);
            for (int i = 0; i < par.Length; i++)
            {
                suma += score[i] - par[i];
                Console.WriteLine(suma);
            }
            return suma;
        }
    }
}