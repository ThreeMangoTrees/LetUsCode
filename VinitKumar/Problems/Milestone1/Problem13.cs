using System;
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public class Problem13
    {
        private int TwoVariableApproach(TreeNode root)
        {
            if (root == null) return -1;
            Queue<TreeNode> q = new();
            int mn = root.val;
            int result = 0;
            q.Enqueue(root);
            while (q.Count > 0)
            {
                TreeNode crnt = q.Dequeue();
                if (crnt.val != mn)
                {
                    if (result == 0)
                    {
                        result = crnt.val;
                    }
                    else
                    {
                        result = Math.Min(result, crnt.val);
                    }
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

            return result == 0 ? -1 : result;
        }

        private int SortedSetApproach(TreeNode root)
        {
            SortedSet<int> sset = new SortedSet<int>();
            Queue<TreeNode> q = new Queue<TreeNode>();
            q.Enqueue(root);

            while (q.Count > 0)
            {
                TreeNode crnt = q.Dequeue();
                sset.Add(crnt.val);
                if (sset.Count > 2)
                {
                    sset.Remove(sset.Max);
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
            return sset.Min == sset.Max ? -1 : sset.Max;
        }

        public int FindSecondMinimumValue(TreeNode root)
        {
            // return FindSecondMinimumValueQueueApproach(root);
            return SortedSetApproach(root);
        }

    }
}

