// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/52597aa56021e91c93000cb0
// # Notes  : tag-codewars
// #-----------------------------------------------------------

using System.Linq;

namespace Codewars
{
    public class MovingZerosToTheEnd
    {
        public static int[] MoveZeroes(int[] arr)
        {
            var numbers = arr.Where(x => x != 0).ToList();
            numbers.AddRange(arr.Where(x => x == 0));
            return numbers.ToArray();
        }
    }
}