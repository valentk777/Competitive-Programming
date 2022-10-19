// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/56919e637b2b971492000036
// # Notes  : tag-codewars, tag-kyu-7
// #-----------------------------------------------------------

using System;

namespace Codewars
{
    public class MarioAdapter : IUnit
    {
        private Mario _mario;

        public MarioAdapter(Mario mario) => _mario = mario;

        public void Attack(Target target) => target.Health -= _mario.jumpAttack();
    }
}