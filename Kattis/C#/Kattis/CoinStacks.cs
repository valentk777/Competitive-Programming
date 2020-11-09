// #-----------------------------------------------------------
// # 
// # https://ncpc20.kattis.com/problems/coinstacks
// # 
// #-----------------------------------------------------------

using System;
using System.Collections.Generic;
using System.Linq;

namespace Kattis
{
    public class CoinStacks
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

        public static void WA(List<object> array)
        {
            foreach (var ob in array)
                Console.WriteLine(ob);
        }

        #endregion

        static void Solve()
        {
            RI();
            var x = RIA();
            if (x.Sum() % 2 != 0)
            {
                WL("no");
                return;
            }

            var ats = new List<string>();
            while (x.Sum() > 0)
            {
                int max = Array.IndexOf(x, x.Max());
                int min = Array.LastIndexOf(x, x.Where(z => z > 0).Min());

                if (max == min)
                {
                    WL("no");
                    return;
                }
                else
                {
                    ats.Add($"{min + 1} {max + 1}");
                    x[max]--;
                    x[min]--;
                }
            }

            WL("yes");
            WA(ats.ToArray());
        }
    }
}
