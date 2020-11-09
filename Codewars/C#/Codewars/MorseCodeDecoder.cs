// #-----------------------------------------------------------
// # 
// # https://www.codewars.com/kata/54b724efac3d5402db00065e
// # 
// #-----------------------------------------------------------

using System.Collections.Generic;

namespace Codewars
{
    public static class MorseCode
    {
        private static Dictionary<string, string> MorseList => new Dictionary<string, string>(){
            {" " , " "},
            { "...---..." , "SOS"},

            { ".-" , "A"},
            { "-..." , "B"},
            { "-.-." , "C"},
            { "-.." , "D"},
            { "." , "E"},
            { "..-." , "F"},
            { "--." , "G"},
            { "...." , "H"},
            { ".." , "I"},
            { ".---" , "J"},
            { "-.-" , "K"},
            { ".-.." , "L"},
            { "--" , "M"},
            { "-." , "N"},
            { "---" , "O"},
            { ".--." , "P"},
            { "--.-" , "Q"},
            { ".-." , "R"},
            { "..." , "S"},
            { "-" , "T"},
            { "..-" , "U"},
            { "...-" , "V"},
            { ".--" , "W"},
            { "-..-" , "X"},
            { "-.--" , "Y"},
            { "--.." , "Z"},

            { "-----" , "0"},
            { ".----" , "1"},
            { "..---" , "2"},
            { "...--" , "3"},
            { "....-" , "4"},
            { "....." , "5"},
            { "-...." , "6"},
            { "--..." , "7"},
            { "---.." , "8"},
            { "----." , "9"},

            { "-.-.--" , "!"},
            { ".--.-." , "@"},
            { "..--.." , "?"},
            { ".-.-.-" , "."},
        };

        public static string Get(string morse) => MorseList[morse];
    }

    public class MorseCodeDecoder
    {
        public static string Decode(string morseCode)
        {
            var split = Split(morseCode.Trim());
            for (int i = 0; i < split.Length; i++)
                split[i] = MorseCode.Get(split[i]);

            return string.Join("", split);
        }

        public static string[] Split(string text)
        {
            var words = new List<string>();

            foreach (var word in text.Split("   "))
            {
                foreach (var letter in word.Split(' '))
                    words.Add(letter);

                words.Add(" ");
            }

            words.RemoveAt(words.Count - 1);
            return words.ToArray();
        }
    }
}
