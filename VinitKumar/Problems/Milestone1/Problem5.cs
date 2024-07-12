using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VinitKumar.Utilities;

namespace VinitKumar.Problems
{
    public class Problem5
    {

        private static bool InOrderTraversalRecursive(TreeNode? Root1, TreeNode? Root2)
        {

            if (Root1 == null && Root2 == null) 
            { 
                return true; 
            }
            else if (Root1 == null && Root2 != null)
            {
                return false;
            }
            else if (Root1 != null && Root2 == null)
            {
                return false;
            }
            else
            {
                if(Root1?.Val != Root2?.Val)
                {
                    return false;
                }
            }

            return InOrderTraversalRecursive(Root1?.Left, Root2?.Left) && InOrderTraversalRecursive(Root1?.Right, Root2?.Right);
        }

        public static bool IsSameTree(TreeNode? Root1, TreeNode? Root2)
        {
            return InOrderTraversalRecursive(Root1, Root2);
            
        }
    }
}
