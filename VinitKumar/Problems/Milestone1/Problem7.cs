using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public class Problem7
    {
        private static int ans;
        private static bool IsLeaf(TreeNode? root)
        {
            return root?.left == null && root?.right == null;
        }
        private static void helper(TreeNode root)
        {
            if (root == null) return;

            if (root.left != null && IsLeaf(root.left))
            {
                ans += root.left.val;
            }

            helper(root.left);
            helper(root.right);
        }
        public int SumOfleftLeaves(TreeNode root)
        {
            ans = 0;
            helper(root);
            return ans;
        }
    }
}
