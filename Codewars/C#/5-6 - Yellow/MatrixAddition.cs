// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/526233aefd4764272800036f
// # Notes  : tag-codewars, tag-kyu-6
// #-----------------------------------------------------------

namespace Codewars
{
    public class MatrixAdditions
    {
        public static int[][] MatrixAddition(int[][] a, int[][] b)
        {
            var length = a.GetLength(0);
            for (var i = 0; i < length; i++)
                for (var j = 0; j < length; j++)
                    a[i][j] += b[i][j];

            return a;
        }
    }
}