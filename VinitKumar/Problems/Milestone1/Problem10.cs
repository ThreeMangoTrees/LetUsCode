using System;


using System;
using VinitKumar.Utilities;

/*
 *  [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)
 */

namespace VinitKumar.Problems.Milestone1
{
	public class Problem10
	{
        IList<IList<int>>? ansR;
        private IList<IList<int>> LevelOrderIterative(TreeNode? root)
        {
            IList<IList<int>> ans = new List<IList<int>>();
            if (root == null)
            {
                return ans;
            }
            Queue<TreeNode> q = new Queue<TreeNode>();
            q.Enqueue(root);
            while (q.Count > 0)
            {
                int qsz = q.Count;
                List<int> tlist = new List<int>();
                while (qsz > 0)
                {
                    TreeNode crnt = q.Dequeue();
                    tlist.Add(crnt.val);

                    if (crnt.left != null)
                    {
                        q.Enqueue(crnt.left);
                    }
                    if (crnt.right != null)
                    {
                        q.Enqueue(crnt.right);
                    }
                    qsz -= 1;
                }
                ans.Add(tlist);
            }
            return ans;
        }
        
        private void LevelOrderRecursive(TreeNode? root, int level)
        {
            if (root == null)
            {
                return;
            }

            if (ansR?.Count == level)
            {
                ansR.Add(new List<int>());
            }

            ansR?[level].Add(root.val);

            LevelOrderRecursive(root?.left, level + 1);
            LevelOrderRecursive(root?.right, level + 1);
        }
        public IList<IList<int>> LevelOrder(TreeNode root)
        {
            // return LevelOrderIterative(root);

            ansR = new List<IList<int>>();
            LevelOrderRecursive(root, 0);
            return ansR;
        }

    }
}
