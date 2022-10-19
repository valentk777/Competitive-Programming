// #-----------------------------------------------------------
// # URL    : https://www.codewars.com/kata/58f39391f4447fe43d00008f
// # Notes  : tag-codewars, tag-kyu-5
// #-----------------------------------------------------------

using System.Collections;

namespace Codewars
{
    public sealed class Adam : Male
    {
        private static Adam _adam = new Adam();

        private Adam() : base("Adam", null, null, true)
        {
        }

        public static Adam GetInstance() => _adam;
    }

    public sealed class Eve : Female
    {
        private static Eve _eve = null;

        private Eve(Adam adam) : base("Eve", null, null, true)
        { }

        public static Eve GetInstance(Adam adam)
        {
            if (adam == null)
                throw new System.ArgumentNullException();

            _eve = _eve == null ? new Eve(adam) : _eve;
            return _eve;
        }
    }

    public class Male : Human
    {
        public Male(string name, Female mother, Male father, bool firstHuman = false) : base(name, mother, father, firstHuman)
        {
        }
    }

    public class Female : Human
    {
        public Female(string name, Female mother, Male father, bool firstHuman = false) : base(name, mother, father, firstHuman)
        {
        }
    }

    public abstract class Human
    {
        public string Name;
        public Female Mother;
        public Male Father;

        public Human(string name, Female mother, Male father, bool firstHuman = false)
        {
            if (!firstHuman)
            {
                if (mother == null)
                    throw new System.ArgumentNullException();

                if (father == null)
                    throw new System.ArgumentNullException();
            }

            Name = name;
            Mother = mother;
            Father = father;
        }
    }
}