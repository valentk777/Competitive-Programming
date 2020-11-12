// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/556deca17c58da83c00002db
// # Notes  : tag-codewars
// #-----------------------------------------------------------

namespace Codewars
{
    public class TribonacciSequence
    {
        public double[] Tribonacci(double[] signature, int n) =>
            (n == 0) ? new double[] { 0 } : (n < 3) ? copyArray(signature, n, n) : getNumberArray(copyArray(signature, 3, n), n);

        private double[] getNumberArray(double[] arr, int n)
        {
            for (int i = 3; i < n; i++)
                arr[i] = arr[i - 3] + arr[i - 2] + arr[i - 1];
            return arr;
        }

        private double[] copyArray(double[] signature, int number, int length)
        {
            double[] arr = new double[length];
            for (int i = 0; i < number; i++)
                arr[i] = signature[i];
            return arr;
        }
    }
}