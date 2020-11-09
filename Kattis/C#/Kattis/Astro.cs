// #-----------------------------------------------------------
// # 
// # https://open.kattis.com/problems/astro
// # 
// #-----------------------------------------------------------

using System;

namespace Kattis
{
    public class Astro
    {
        static void Solve()
        {
            var start1 = Console.ReadLine().ToTime();
            var start2 = Console.ReadLine().ToTime();
            var move1 = Console.ReadLine().ToTime();
            var move2 = Console.ReadLine().ToTime();

            var start2Multiplayer = SolutionUtils.FindMultiplayer(start1.TotalMinutes, start2.TotalMinutes, move1.TotalMinutes, move2.TotalMinutes);

            if (start2Multiplayer == 0)
            {
                Console.WriteLine("Never");
            }
            else
            {
                var meetUpTime = start2 + move2 * start2Multiplayer;
                Console.WriteLine(meetUpTime.Days.GetWeekDay());
                Console.WriteLine($"{meetUpTime.Hours:00}:{meetUpTime.Minutes:00}");
            }
        }
    }

    public static class SolutionUtils
    {
        public static TimeSpan ToTime(this string time) => new TimeSpan(0, int.Parse(time.Split(':')[0]), int.Parse(time.Split(':')[1]), 0);

        public static int FindMultiplayer(double start1, double start2, double move1, double move2)
        {
            int start2Multiplayer = 1;
            double number = (start2 - start1 + move2 * start2Multiplayer) % move1;
            while (number != 0 && start2Multiplayer < 700)
            {
                start2Multiplayer++;
                number = (start2 - start1 + move2 * start2Multiplayer) % move1;
            }

            return start2Multiplayer < 700 ? start2Multiplayer : 0;
        }

        public static string GetWeekDay(this int day)
        {
            switch (day % 7)
            {
                case 0:
                    return "Saturday";
                case 1:
                    return "Sunday";
                case 2:
                    return "Monday";
                case 3:
                    return "Tuesday";
                case 4:
                    return "Wednesday";
                case 5:
                    return "Thursday";
                case 6:
                    return "Friday";
                default:
                    return "";
            };
        }
    }
}
