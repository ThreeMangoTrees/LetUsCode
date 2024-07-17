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
        public static int MaxDepth(TreeNode? root)
        {
            if (root == null) return 0;
            return 1 + Math.Max(MaxDepth(root?.Left), MaxDepth(root?.Right));
        }
    }
}
