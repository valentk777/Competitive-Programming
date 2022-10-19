// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/53222010db0eea35ad000001
// # Notes  : tag-codewars, tag-kyu-7
// #-----------------------------------------------------------

using System;

namespace Codewars
{
    public static class Kata
    {
        public static double? GetSlope(Point p1, Point p2)
        {
            if (p1.X == p2.X || (p1.Y == p2.Y && p1.X == p2.X))
                return null;

            return (p1.Y - p2.Y) / (p1.X - p2.X);
        }
    }
}