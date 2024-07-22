using System;
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public class Problem13
    {
        public static int FindSecondMinimumValue(TreeNode root)
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
                    else if (crnt.val < result)
                    {
                        result = crnt.val;
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

    }
}

