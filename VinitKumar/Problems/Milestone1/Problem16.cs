using System;
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public class Problem16
    {
        private static IList<double> Iterative(TreeNode? root)
        {
            IList<double> lst = new List<double>();
            if (root == null)
            {
                return lst;
            }

            Queue<TreeNode> q = new Queue<TreeNode>();
            q.Enqueue(root);
            while (q.Count > 0)
            {
                int sz = q.Count;
                double sum = 0.0;
                for (int i = 0; i < sz; i++)
                {
                    TreeNode crnt = q.Dequeue();
                    sum += crnt.val;
                    if (crnt.left != null)
                    {
                        q.Enqueue(crnt.left);
                    }
                    if (crnt.right != null)
                    {
                        q.Enqueue(crnt.right);
                    }
                }
                double avg = sum / sz;
                lst.Add(avg);
            }
            return lst;
        }

        private static IList<Tuple<double, int>> sumCount;
        private static void Recursive(TreeNode? root, int level)
        {
            if (root == null) return;
            if (sumCount.Count == level)
            {
                sumCount.Add(new Tuple<double, int>(root.val, 1));
            }
            else
            {
                (double sum, int count) = sumCount[level];
                sumCount[level] = new Tuple<double, int>(sum + root.val, count + 1);
            }

            Recursive(root.left, level + 1);
            Recursive(root.right, level + 1);
        }

        public IList<double> AverageOfLevels(TreeNode? root)
        {
            //return Iterative(root);

            IList<double> ans = new List<double>();
            sumCount = new List<Tuple<double, int>>();
            Recursive(root, 0);

            foreach (var tup in sumCount)
            {
                double avg = tup.Item1 / tup.Item2;
                ans.Add(avg);
            }
            return ans;

        }
    }
}