// #-----------------------------------------------------------
// #
// # https://www.codewars.com/kata/52774a314c2333f0a7000688
// #
// #-----------------------------------------------------------

using System.Collections;

namespace Codewars
{
    public class ValidateParentheses
    {
        public static bool ValidParentheses(string input)
        {
            var stack = new Stack();
            foreach (var i in input)
            {
                if (i == ')')
                    if (stack.Count == 0)
                        return false;
                    else
                        stack.Pop();

                if (i == '(')
                    stack.Push(1);
            }

            return stack.Count == 0;
        }
    }
}