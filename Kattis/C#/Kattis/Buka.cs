// #-----------------------------------------------------------
// # URL    : https://open.kattis.com/problems/buka
// # Notes  : tag-kattis
// #-----------------------------------------------------------

using System;
using System.Text;

namespace Kattis
{
    public class Buka
    {
        static void Solve()
        {
            StringBuilder A = new StringBuilder(Console.ReadLine());
            var character = Console.ReadLine();
            StringBuilder B = new StringBuilder(Console.ReadLine());

            if (character == "+")
            {
                if (A.Length > B.Length)
                    Sum(A, B);
                else
                    Sum(B, A);
            }
            else
            {
                Console.Write(1);
                for (int i = 0; i < A.Length + B.Length - 2; i++)
                    Console.Write(0);
            }
        }

        static void Sum(StringBuilder A, StringBuilder B)
        {
            int plus = 0;
            int diff = A.Length - B.Length;
            for (int i = A.Length - 1; i >= 0; i--)
            {
                int sum;
                if (i - diff < 0)
                    if (plus == 0)
                        break;
                    else
                        sum = A[i] + plus;
                else
                    sum = A[i] + B[i - diff] + plus;

                if (sum == 97)
                    A[i] = '1';
                else if (sum == 98)
                    A[i] = '2';
            }

            for (int i = 0; i < A.Length; i++)
                Console.Write(A[i]);
        }
    }
}
