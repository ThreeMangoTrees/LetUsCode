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
            BinaryTreeRoot.left = new TreeNode(20);
            BinaryTreeRoot.right = new TreeNode(30);
            BinaryTreeRoot.left.left = new TreeNode(40);
            BinaryTreeRoot.left.right = new TreeNode(50);
            BinaryTreeRoot.right.left = new TreeNode(60);
            BinaryTreeRoot.right.right = new TreeNode(70);
            return BinaryTreeRoot; 
        }

        public static TreeNode CreateBinarySearchTree()
        {
            TreeNode BinaryTreeRoot = new TreeNode(100);
            BinaryTreeRoot.left = new TreeNode(50);
            BinaryTreeRoot.right = new TreeNode(150);
            BinaryTreeRoot.left.left = new TreeNode(30);
            BinaryTreeRoot.left.right = new TreeNode(75);
            BinaryTreeRoot.right.left = new TreeNode(125);
            BinaryTreeRoot.right.right = new TreeNode(175);
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
