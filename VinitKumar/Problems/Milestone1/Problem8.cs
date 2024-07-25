using System;
using VinitKumar.Utilities;

/*
 * [112. Path Sum](https://leetcode.com/problems/path-sum/)
 */


namespace VinitKumar.Problems.Milestone1
{
	public class Problem8
    {
        public bool HasPathSum(TreeNode root, int targetSum)
        {
            if (root == null) return false;
            if (root.left == null && root.right == null && targetSum - root.val == 0) return true;
            return HasPathSum(root.left, targetSum - root.val) || HasPathSum(root.right, targetSum - root.val);
        }
    }
}
