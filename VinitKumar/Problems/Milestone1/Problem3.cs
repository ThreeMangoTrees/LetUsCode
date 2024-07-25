using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public class Problem3
    {
        public static void PreOrder(TreeNode? Root)
        {
            if (Root != null)
            {
                Console.Write($"{Root.val}, ");
                PreOrder(Root.left);
                PreOrder(Root.right);
            }
        }

        public static void InOrder(TreeNode? Root)
        {
            if (Root != null)
            {
                InOrder(Root.left);
                Console.Write($"{Root.val}, ");
                InOrder(Root.right);
            }
        }

        public static void PostOrder(TreeNode? Root)
        {
            if (Root != null)
            {
                PostOrder(Root.left);
                PostOrder(Root.right);
                Console.Write($"{Root.val}, ");
            }
        }
    }
}
