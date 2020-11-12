// #-----------------------------------------------------------
// # URL    : https://open.kattis.com/problems/avion
// # Notes  : tag-kattis
// #-----------------------------------------------------------

using System;

namespace Kattis
{
    public class Avion
    {
        static void Solve()
        {
            var found = false;
            for (var i = 0; i < 5; i++)
                if (Console.ReadLine().Contains("FBI"))
                {
                    Console.Write($"{i + 1} ");
                    found = true;
                }

            if (!found)
                Console.WriteLine("HE GOT AWAY!");
        }
    }
}
