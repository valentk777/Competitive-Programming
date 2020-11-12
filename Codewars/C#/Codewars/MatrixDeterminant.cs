// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/52a382ee44408cea2500074c
// # Notes  : tag-codewars
// #-----------------------------------------------------------

namespace Codewars
{
    public class MatrixDeterminant
    {
        public static int Determinant(int[][] matrix)
        {
            if (matrix.Length == 1)
                return matrix[0][0];

            int result = 0;
            for (int i = 0; i < matrix.Length; i++)
            {
                int mult = i % 2 == 0 ? 1 : -1;
                result += mult * matrix[0][i] * Determinant(GetMinot(matrix, i));
            }

            return result;
        }

        public static int[][] GetMinot(int[][] matrix, int col)
        {
            var newMatrix = new int[matrix.Length - 1][];
            for (int i = 0; i < matrix.Length - 1; i++)
                newMatrix[i] = Shift(matrix[i + 1], col);

            return newMatrix;
        }

        public static int[] Shift(int[] row, int removeAt)
        {
            var newRow = new int[row.Length - 1];
            for (int i = 0; i < removeAt; i++)
                newRow[i] = row[i];

            for (int i = removeAt; i < row.Length - 1; i++)
                newRow[i] = row[i + 1];
            return newRow;
        }
    }
}