// #-----------------------------------------------------------
// # 
// # https://open.kattis.com/problems/digits
// # 
// #-----------------------------------------------------------

using System;

namespace Kattis
{
    public class Digits
    {
        static void Solve()
        {
            var sk0 = Console.ReadLine();
            while (sk0 != "END")
            {
                var sk1 = sk0.Length.ToString();
                var i = 1;
                while (sk0 != sk1)
                {
                    sk0 = sk1;
                    sk1 = sk1.Length.ToString();
                    i++;
                }

                Console.WriteLine(i);
                sk0 = Console.ReadLine();
            }
        }
    }
}
