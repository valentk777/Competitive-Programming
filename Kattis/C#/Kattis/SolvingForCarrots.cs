// #-----------------------------------------------------------
// # 
// # https://open.kattis.com/problems/carrots
// # 
// #-----------------------------------------------------------

using System;
using System.Linq;

namespace Kattis
{
    public class SolvingForCarrots
    {
        #region Helpers

        public static string RL() => Console.ReadLine();

        public static void WL(object text) => Console.WriteLine(text);

        public static int RI() => int.Parse(Console.ReadLine());

        public static string[] RA() => Console.ReadLine().Split();

        public static int[] RIA() => Console.ReadLine().Split().Select(x => int.Parse(x)).ToArray();

        public static void WA(object[] array)
        {
            foreach (var ob in array)
                Console.WriteLine(ob);
        }

        #endregion

        static void Solve()
        {
            var x = RIA();
            var n = x[0];
            var p = x[1];
            for (int i = 0; i < n; i++)
                RL();
            WL(p);
        }
    }
}
