// #-----------------------------------------------------------
// # 
// # https://www.codewars.com/kata/52685f7382004e774f0001f7
// # 
// #-----------------------------------------------------------

namespace Codewars
{
    public class HumanReadableTime
    {
        public static string GetReadableTime(int seconds)
        {
            int HH = seconds / 3600;
            seconds = seconds - HH * 3600;
            int MM = seconds / 60;
            int SS = seconds - MM * 60;
            return $"{HH:D2}:{MM:D2}:{SS:D2}";
        }
    }
}
