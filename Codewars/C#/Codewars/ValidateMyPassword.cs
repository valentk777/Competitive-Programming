// #-----------------------------------------------------------
// # 
// # https://www.codewars.com/kata/59c01248bf10a47bd1000046
// # 
// #-----------------------------------------------------------

namespace Codewars
{
    public class ValidateMyPassword
    {
        public static string validator(string password)
        {
            if (password.Length < 4 || password.Length > 19)
                return "INVALID";

            var letter = false;
            var number = false;
            foreach (var l in password)
            {
                if (!char.IsLetterOrDigit(l))
                    return "INVALID";

                if (char.IsLetter(l))
                    letter = true;

                if (char.IsDigit(l))
                    number = true;
            }

            if (!letter || !number)
                return "INVALID";

            return "VALID";
        }
    }
}
