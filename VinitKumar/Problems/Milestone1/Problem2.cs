using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VinitKumar.Utilities;

namespace VinitKumar.Problems
{
    public class Problem2
    {
        public void PreOrder(TreeNode? Root)
        {
            if(Root != null)
            {
                Console.Write($"{Root.Val}, ");
                PreOrder(Root.Left);
                PreOrder(Root.Right);
            }
        }

        public void PostOrder(TreeNode? Root)
        {
            if(Root != null)
            {
                PostOrder(Root.Left);
                PostOrder(Root.Right);
                Console.Write($"{Root.Val}, ");
            }
        }
    }
}
