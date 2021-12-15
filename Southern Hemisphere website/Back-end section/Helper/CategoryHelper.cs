using System;
using System.Text;

namespace _ass1.Helper
{
    public class CategoryHelper
    {
        public static string Filter(string s)
        {
            string[] subStrings = s.Split(',');
            for (int i = 0; i < subStrings.Length; i++)
            {
                subStrings[i] = subStrings[i].Trim();
            }
            StringBuilder newString = new StringBuilder();
            foreach (string x in subStrings)
            {
                newString.Append(x).Append(",");
            }
            newString.Remove(newString.Length - 1, 1);
            return newString.ToString();
        }
    }
}
