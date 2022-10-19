// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
// # Notes  : tag-codewars, tag-kyu-7
// #-----------------------------------------------------------

using System;
using System.Text.RegularExpressions;

namespace Codewars
{
    public class ValidatePin
    {
        public static bool ValidatePin(string pin)
        {
            return new Regex(@"^\d{4}$|^\d{6}$").Match(pin).Success;
        }
    }
}