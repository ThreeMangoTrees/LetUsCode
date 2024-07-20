using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VinitKumar.Utilities;

namespace VinitKumar.Problems
{
    public class Problem4
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
