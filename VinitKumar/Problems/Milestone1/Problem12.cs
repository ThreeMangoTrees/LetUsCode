using System;
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public static class Problem12
    {
        private static TreeNode SearchBSTIterative(TreeNode? root, int val)
        {
            if (root == null) return null;

            Queue<TreeNode> q = new Queue<TreeNode>();
            q.Enqueue(root);
            while (q.Count > 0)
            {
                TreeNode crnt = q.Dequeue();
                if (crnt.val == val)
                {
                    return crnt;
                }
                if (crnt.left != null)
                {
                    q.Enqueue(crnt.left);
                }
                if (crnt.right != null)
                {
                    q.Enqueue(crnt.right);
                }
            }
            return null;
        }

        private static TreeNode SearchBSTRecursive(TreeNode? root, int val)
        {
            if (root == null) return null;
            if (root?.val == val) return root;
            TreeNode? left = SearchBSTRecursive(root?.left, val);
            TreeNode? right = SearchBSTRecursive(root?.right, val);
            return left != null ? left : right;
        }

        public static TreeNode SearchBST(TreeNode root, int val)
        {
            // return SearchBSTIterative(root, val);
            return SearchBSTRecursive(root, val);
        }
    }
}
