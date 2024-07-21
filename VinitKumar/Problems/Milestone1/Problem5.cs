using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public class Problem5
    {
        private static bool Traverse(TreeNode? left, TreeNode? right)
        {
            if(left is null && right is null)
            {
                return true;
            }

            if(left?.val != right?.val)
            {
                return false;
            }

            return Traverse(left?.left, right?.right) && Traverse(left?.right, right?.left);
            
        }

        public static bool IsSymmetric(TreeNode? Root)
        {
            if(Root is null)
            {
                return true;
            }
            return Traverse(Root?.left, Root?.right);
        }
    }
}
