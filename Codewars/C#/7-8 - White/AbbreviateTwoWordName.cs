// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
// # Notes  : tag-codewars, tag-kyu-8
// #-----------------------------------------------------------

using System;

namespace Codewars
{
    public class Kata
    {
        public static string AbbrevName(string name)
        {
            var t = name.Split();
            return $"{Char.ToUpper(t[0][0])}.{Char.ToUpper(t[1][0])}";
        }
    }
}