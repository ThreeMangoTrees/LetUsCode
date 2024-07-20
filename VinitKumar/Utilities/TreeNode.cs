using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VinitKumar.Utilities
{
    public class TreeNode(int Value)
    {
        public int val { get; set; } = Value;
        public TreeNode? left { get; set; } = null;
        public TreeNode? right { get; set; } = null;
    }
}
