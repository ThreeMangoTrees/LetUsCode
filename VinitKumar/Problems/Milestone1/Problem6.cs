using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VinitKumar.Utilities;

namespace VinitKumar.Problems
{
    public class Problem6
    {
        private static bool Traverse(TreeNode? Left, TreeNode? Right)
        {
            if(Left is null && Right is null)
            {
                return true;
            }

            if(Left?.Val != Right?.Val)
            {
                return false;
            }

            return Traverse(Left?.Left, Right?.Right) && Traverse(Left?.Right, Right?.Left);
            
        }

        public static bool IsSymmetric(TreeNode? Root)
        {
            if(Root is null)
            {
                return true;
            }
            return Traverse(Root?.Left, Root?.Right);
        }
    }
}
