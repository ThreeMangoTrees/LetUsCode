using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public class Problem8
    {
        private static int ans;
        private static bool IsLeaf(TreeNode? root)
        {
            return root?.Left == null && root?.Right == null;
        }
        private static void helper(TreeNode root)
        {
            if (root == null) return;

            if (root.Left != null && IsLeaf(root.Left))
            {
                ans += root.Left.Val;
            }

            helper(root.Left);
            helper(root.Right);
        }
        public int SumOfLeftLeaves(TreeNode root)
        {
            ans = 0;
            helper(root);
            return ans;
        }
    }
}
