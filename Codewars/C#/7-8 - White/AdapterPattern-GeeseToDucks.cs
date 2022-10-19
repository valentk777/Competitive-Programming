// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/5792e2e93467db66a000009f
// # Notes  : tag-codewars, tag-kyu-7
// #-----------------------------------------------------------

namespace Codewars
{
    public class GooseToIDuckAdapter : IDuck
    {
        private Goose goose;

        public GooseToIDuckAdapter(Goose goose) => this.goose = goose;

        public string Quack() => goose.Honk();

        public void Fly() => goose.Fly();
    }
}