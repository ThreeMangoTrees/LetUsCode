using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VinitKumar.Utilities
{
    public static class TreeHelper
    {
        public static TreeNode CreateBinaryTree()
        {
            TreeNode BinaryTreeRoot = new TreeNode(10);
            BinaryTreeRoot.Left = new TreeNode(20);
            BinaryTreeRoot.Right = new TreeNode(30);
            BinaryTreeRoot.Left.Left = new TreeNode(40);
            BinaryTreeRoot.Left.Right = new TreeNode(50);
            BinaryTreeRoot.Right.Left = new TreeNode(60);
            BinaryTreeRoot.Right.Right = new TreeNode(70);
            return BinaryTreeRoot; 
        }
    }
}
