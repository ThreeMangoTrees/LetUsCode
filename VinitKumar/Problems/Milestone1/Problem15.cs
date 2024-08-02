using System;
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public class Problem15 { 
        private static bool ans;
        private static int Helper(TreeNode? root)
        {
            if (root == null) return 0;

            int left = Helper(root.left);
            int right = Helper(root.right);

            if (Math.Abs(left - right) > 1) ans = false;

            return 1 + Math.Max(left, right);
        }

        public static bool IsBalanced(TreeNode? root)
        {
            ans = true;
            Helper(root);
            return ans;
        }
    }
}