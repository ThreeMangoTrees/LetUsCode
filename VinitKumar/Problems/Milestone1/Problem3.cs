using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VinitKumar.Utilities;

namespace VinitKumar.Problems
{
    public class Problem3
    {
        public static void PreOrder(TreeNode? Root)
        {
            if (Root != null)
            {
                Console.Write($"{Root.Val}, ");
                PreOrder(Root.Left);
                PreOrder(Root.Right);
            }
        }

        public static void InOrder(TreeNode? Root)
        {
            if (Root != null)
            {
                InOrder(Root.Left);
                Console.Write($"{Root.Val}, ");
                InOrder(Root.Right);
            }
        }

        public static void PostOrder(TreeNode? Root)
        {
            if (Root != null)
            {
                PostOrder(Root.Left);
                PostOrder(Root.Right);
                Console.Write($"{Root.Val}, ");
            }
        }
    }
}
