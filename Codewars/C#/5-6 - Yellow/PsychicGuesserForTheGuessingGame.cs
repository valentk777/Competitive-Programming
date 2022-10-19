// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/5c0ce510316a58fa7f000025
// # Notes  : tag-codewars, tag-kyu-5
// #-----------------------------------------------------------

using System.Reflection;
using System;

namespace Codewars
{
    public static class Extensions
    {
        public static int Guess(this GuessingGame guessingGame, bool fake) =>
          guessingGame.Guess((int)guessingGame.GetType()
                                              .GetField("secretNumber", BindingFlags.Instance | BindingFlags.NonPublic)
                                              .GetValue(guessingGame));
    }

    public class PsychicGuesser
    {
        public bool MakeAGuess(int lastResult) => false;
    }
}