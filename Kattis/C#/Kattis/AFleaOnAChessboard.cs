// #-----------------------------------------------------------
// # 
// # https://open.kattis.com/problems/fleaonachessboard
// # 
// #-----------------------------------------------------------

using System;

namespace Kattis
{
    public class AFleaOnAChessboard
    {
        static void Solve()
        {
            var data = Console.ReadLine();
            while (data != "0 0 0 0 0")
            {
                var dataSplit = data.Split();
                int s = int.Parse(dataSplit[0]);
                int x = int.Parse(dataSplit[1]);
                int y = int.Parse(dataSplit[2]);
                int dx = int.Parse(dataSplit[3]);
                int dy = int.Parse(dataSplit[4]);

                int jump = 0;
                int xdx = x.Normalized(0, s);
                int ydy = y.Normalized(0, s);
                bool first = true;

                int xn = xdx;
                int yn = ydy;
                while (IsBlack(s, xdx, ydy) && (xdx != xn || ydy != yn || first))
                {
                    jump++;
                    xdx = xdx.Normalized(dx, s);
                    ydy = ydy.Normalized(dy, s);
                    first = false;
                }

                if (IsBlack(s, xdx, ydy))
                    Console.WriteLine("The flea cannot escape from black squares.");
                else
                    Console.WriteLine($"After {jump} jumps the flea lands at ({x + jump * dx}, {y + jump * dy}).");

                data = Console.ReadLine();
            }
        }

        private static bool IsBlack(int S, int x, int y) =>
            x % S == 0 || y % S == 0 || (x - S > 0 && y - S > 0) || (x - S < 0 && y - S < 0);
    }

    public static class Ext
    {
        public static int Normalized(this int i, int di, int si) => (i + di) % (2 * si);
    }
}
