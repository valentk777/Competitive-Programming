// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
// # Notes  : tag-codewars, tag-kyu-7
// #-----------------------------------------------------------

using System;
using System.Collections.Generic;
using System.Linq;

namespace Codewars
{
    public class Kata
    {
        public static IEnumerable<string> OpenOrSenior(int[][] data)
        {
            var li = new List<string>();
            foreach (var el in data)
            {
                if ((el[0] > 54) && (el[1] > 7))
                {
                    li.Add("Senior");
                }
                else
                {
                    li.Add("Open");
                }
            }
            return li;
        }
    }
}