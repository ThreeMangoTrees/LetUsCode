using System;
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public static class Problem12
    {
        public static TreeNode? SearchBST(TreeNode? root, int val)
        {
            if (root == null) return null;
            if (root?.val == val) return root;
            TreeNode? left = SearchBST(root?.left, val);
            TreeNode? right = SearchBST(root?.right, val);
            return left ?? right;
        }
    }
}
