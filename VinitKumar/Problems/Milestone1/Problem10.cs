using System;
using VinitKumar.Utilities;

/*
 *  [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/description/)
 */
public class Problem10
{
    List<IList<int>> ans = new List<IList<int>>();
    private void Recursion(TreeNode root, List<int> tlist, int ts)
    {
        if (root == null)
        {
            return;
        }

        tlist.Add(root.val);
        if (root.left == null && root.right == null && ts == root.val)
        {
            ans.Add(new List<int>(tlist));
        }


        Recursion(root.left, tlist, ts - root.val);
        Recursion(root.right, tlist, ts - root.val);

        tlist.RemoveAt(tlist.Count - 1);
    }

    public IList<IList<int>> PathSum(TreeNode root, int targetSum)
    {
        List<int> tl = new List<int>();
        Recursion(root, tl, targetSum);
        return ans;
    }
}
