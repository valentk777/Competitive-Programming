// #-----------------------------------------------------------
// # 
// # https://open.kattis.com/problems/electricaloutlets
// # 
// #-----------------------------------------------------------

using System;
using System.Linq;

namespace Kattis
{
    public class ElectricalOutlets
    {
        static void Solve()
        {
            var N = int.Parse(Console.ReadLine());

            for(int i = 0; i < N; i++)
            {
                var sum = 0;
                var Oi = Console.ReadLine().Split().Select(x => int.Parse(x)).ToArray();
                for (int j = 1; j < Oi.Length; j++)
                    sum += Oi[j] - 1;

                Console.WriteLine(sum + 1);
            }
        }
    }
}
