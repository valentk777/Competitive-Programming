// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/5b358a1e228d316283001892
// # Notes  : tag-codewars, tag-kyu-7
// #-----------------------------------------------------------

using System;
using System.Linq;
using System.Collections.Generic;

namespace Codewars
{
    public class Kata
    {
        public static string GetStrings(string city)
        {
            var dict = new Dictionary<char, string>();
            foreach (char c in city.ToLower())
            {
                if (Char.ToString(c) == " ")
                    continue;
                if (!dict.ContainsKey(c))
                    dict.Add(c, "*");
                else
                    dict[c] += "*";
            }

            string result = "";
            foreach (var kvp in dict)
                result += kvp.Key + ":" + kvp.Value + ",";

            return result[..^1];
        }
    }
}