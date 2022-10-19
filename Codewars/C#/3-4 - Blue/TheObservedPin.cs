// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/5263c6999e0f40dee200059d
// # Notes  : tag-codewars, tag-kyu-4
// #-----------------------------------------------------------

using System.Collections;

namespace Codewars
{
    using System.Collections.Generic;
    using System;
    using System.Linq;

    public class Kata
    {
        public static List<string> GetPINs(string observed)
        {
            var n = observed.Length;
            var intList = observed.Select(x => (int)Char.GetNumericValue(x)).ToList();
            List<List<int>> options = new List<List<int>>();
            var rez = new List<string>();

            foreach (int e in intList)
            {
                options.Add(GetNumbers(e));
            }

            return Generate(options);
        }

        static private List<string> Generate(List<List<int>> dataList)
        {
            List<string> resultList = new List<string>();

            Process(0, dataList, resultList, "");

            return resultList;
        }

        static private void Process(int listIndex, List<List<int>> dataList, List<string> resultList, string result)
        {
            if (listIndex == dataList.Count)
            {
                resultList.Add(result);
                return;
            }

            List<int> currentLevelList = dataList[listIndex];
            for (int i = 0; i < currentLevelList.Count; i++)
                Process(listIndex + 1, dataList, resultList, result + currentLevelList[i]);
        }

        private static List<int> GetNumbers(int n)
        {
            if (n == 0)
                return new List<int>() { 0, 8 };

            var list = new List<int>();
            var matrix = new int[4, 3] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 }, { -1, 0, -1 } };
            int col = (n - 1) % 3;
            int row = (n - 1) / 3;

            for (int i = -1; i < 2; i += 2)
            {
                if ((col + i > -1) && (col + i < 3) && (matrix[row, col + i] != -1))
                    list.Add(matrix[row, col + i]);
                if ((row + i > -1) && (row + i < 4) && (matrix[row + i, col] != -1))
                    list.Add(matrix[row + i, col]);
            }
            list.Add(matrix[row, col]);
            return list;
        }
    }
}