// #-----------------------------------------------------------
// # 
// # https://www.codewars.com/kata/550f22f4d758534c1100025a
// # 
// #-----------------------------------------------------------

using System.Collections.Generic;

namespace Codewars
{
    public class DirectionsReduction
    {
        public static List<string> clean(List<string> arr)
        {

            List<string> arr2 = new List<string>() { };
            for (var i = 1; i < arr.Count; i++)
            {
                var dest = arr[i - 1] + arr[i];
                if (dest == "NORTHSOUTH" || dest == "SOUTHNORTH" ||
                    dest == "WESTEAST" || dest == "EASTWEST")
                    i++;
                else
                    arr2.Add(arr[i - 1]);

                if (i + 1 == arr.Count)
                    arr2.Add(arr[arr.Count - 1]);
            }

            return arr2;
        }

        public static string[] dirReduc(string[] arr)
        {
            int countArr = arr.Length;
            List<string> arr2 = new List<string>(arr);
            while (true)
            {
                arr2 = clean(arr2);
                int countList = arr2.Count;
                if (countList == countArr || countList == 1)
                    break;

                countArr = countList;
            }

            return arr2.ToArray();
        }
    }
}
