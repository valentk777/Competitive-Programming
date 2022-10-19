// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/5497a3c181dd7291ce000700
// # Notes  : tag-codewars, tag-kyu-7
// #-----------------------------------------------------------

using System;

namespace Codewars
{
    public static class Kata
    {
        public static int DiagonalSum(int[,] matrix)
        {
            var suma = 0;
            for (var i = 0; i < matrix.GetLength(0); i++)
                suma += matrix[i, i];

            return suma;
        }
    }
}