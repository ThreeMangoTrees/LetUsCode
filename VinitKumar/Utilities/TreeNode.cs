using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VinitKumar.Utilities
{
    public class TreeNode(int Value)
    {
        public int Val { get; set; } = Value;
        public TreeNode? Left { get; set; } = null;
        public TreeNode? Right { get; set; } = null;
    }
}
