// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/53dc54212259ed3d4f00071c
// # Notes  : tag-codewars, tag-kyu-8
// #-----------------------------------------------------------

namespace Codewars
{
    public class Kata
    {
        public static double SumArray(double[] array)
        {
            double suma = 0;
            foreach (double e in array)
                suma += e;
            return suma;
        }
    }
}