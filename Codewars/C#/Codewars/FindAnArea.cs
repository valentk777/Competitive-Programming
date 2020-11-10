// #-----------------------------------------------------------
// #
// # https://www.codewars.com/kata/59b166f0a35510270800018d
// #
// #-----------------------------------------------------------

using System;
using System.Collections.Generic;

namespace Codewars
{
    public class Point
    {
        public Point(double x, double y)
        {
            X = x;
            Y = y;
        }

        public double X { get; set; }
        public double Y { get; set; }
    }

    public class FindAnArea
    {
        public static double FindArea(List<Point> points)
        {
            double result = 0;
            for (int i = 1; i < points.Count; i++)
            {
                var xdif = points[i].X - points[i - 1].X;
                result += xdif * Math.Min(points[i - 1].Y, points[i].Y);
                result += xdif * Math.Abs(points[i - 1].Y - points[i].Y) / 2;
            }

            return result;
        }
    }
}