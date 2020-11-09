// #-----------------------------------------------------------
// # 
// # https://www.codewars.com/kata/54b72c16cd7f5154e9000457
// # 
// #-----------------------------------------------------------

using System;
using System.Linq;

namespace Codewars
{
    public class MorseCodeDecoderAdvanced
    {
        public static string DecodeBits(string bits)
        {
            bits = bits.Trim('0');
            if (bits.Length == 0)
                return "";

            var units = bits.Split(new[] { "0" }, StringSplitOptions.RemoveEmptyEntries).Select(x => x.Length).Distinct().ToList();
            units.AddRange(bits.Split(new[] { "1" }, StringSplitOptions.RemoveEmptyEntries).Select(x => x.Length).Distinct().ToList());

            var unit = units.Min();
            var words = bits.Split(new[] { new string('0', unit * 7) }, StringSplitOptions.None);

            return string.Join("   ", words
                .Select(word => word.Split(new string('0', unit * 3))
                    .Select(letters => letters.Split(new string('0', unit))
                        .Select(characters => characters.Length == unit ? "." : "-")
                        )
                    .Select(letters => string.Join("", letters)
                    )
                ).Select(word => string.Join(" ", word))
                .ToList());
        }

        public static string DecodeMorse(string morseCode)
        {
            var words = morseCode.Trim().Split(new[] { "   " }, StringSplitOptions.None);
            var translatedWords = words
                .Select(word => word.Split(' '))
                .Select(letters => string.Join("", letters.Select(MorseCode.Get)))
                .ToList();
            return string.Join(" ", translatedWords);
        }
    }
}
