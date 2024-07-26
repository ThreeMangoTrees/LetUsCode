using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public class Problem2
    {
        public void PreOrder(TreeNode? Root)
        {
            if(Root != null)
            {
                Console.Write($"{Root.val}, ");
                PreOrder(Root.left);
                PreOrder(Root.right);
            }
        }

        public void PostOrder(TreeNode? Root)
        {
            if(Root != null)
            {
                PostOrder(Root.left);
                PostOrder(Root.right);
                Console.Write($"{Root.val}, ");
            }
        }
    }
}
