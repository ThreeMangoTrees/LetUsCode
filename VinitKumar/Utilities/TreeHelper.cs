using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VinitKumar.Utilities
{
    public static class TreeHelper
    {
        private static TreeNode? Root = null;
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

        public static TreeNode CreateBinarySearchTree()
        {
            TreeNode BinaryTreeRoot = new TreeNode(100);
            BinaryTreeRoot.Left = new TreeNode(50);
            BinaryTreeRoot.Right = new TreeNode(150);
            BinaryTreeRoot.Left.Left = new TreeNode(30);
            BinaryTreeRoot.Left.Right = new TreeNode(75);
            BinaryTreeRoot.Right.Left = new TreeNode(125);
            BinaryTreeRoot.Right.Right = new TreeNode(175);
            return BinaryTreeRoot;
        }

        public static void InsertIntoBinaryTree(TreeNode? Current)
        {

        }

        public static void InsertIntoBinarySearchTree(TreeNode? Current)
        {

        }
    }
}
