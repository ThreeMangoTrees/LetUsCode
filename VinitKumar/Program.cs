

using VinitKumar.Problems;
using VinitKumar.Utilities;


Console.WriteLine("Problem 6");

TreeNode? treeNode = new TreeNode(1);
treeNode.left = new TreeNode(2);
treeNode.right = new TreeNode(2);
treeNode.left.left = new TreeNode(3);
treeNode.left.right = new TreeNode(4);
treeNode.right.left = new TreeNode(4);
treeNode.right.right = new TreeNode(3);
Console.WriteLine($"IsSymmetric tree ? - {Problem6.IsSymmetric(treeNode)}");


Console.WriteLine("Problem 5");

TreeNode? treeNode1 = new TreeNode(1);
treeNode1.left = new TreeNode(2);
treeNode1.right = new TreeNode(3);
treeNode1.left.left = new TreeNode(4);
treeNode1.left.right = new TreeNode(5);
treeNode1.right.left = new TreeNode(6);
treeNode1.right.right = new TreeNode(7);
TreeNode? treeNode2 = new TreeNode(1);
treeNode2.left = new TreeNode(2);
treeNode2.right = new TreeNode(3);
treeNode2.left.left = new TreeNode(4);
treeNode2.left.right = new TreeNode(5);
treeNode2.right.left = new TreeNode(6);
treeNode2.right.right = new TreeNode(7);
Console.WriteLine($"IsSame tree ? - {Problem5.IsSameTree(treeNode1, treeNode2)}");


Console.WriteLine("Problem 4");


Console.WriteLine("Problem 3");

Console.WriteLine("---- PreOrder Traversal ----");
Problem3.PreOrder(TreeHelper.CreateBinarySearchTree());
Console.WriteLine("\n---- InOrder Traversal ----");
Problem3.InOrder(TreeHelper.CreateBinarySearchTree());
Console.WriteLine("\n---- PostOrder Traversal ----");
Problem3.PostOrder(TreeHelper.CreateBinarySearchTree());

/* 
Problem 2 

Problem2 problem2Instance = new();
TreeNode? BinaryTreeRoot = TreeHelper.CreateBinaryTree();
Console.WriteLine("\n---- PreOrder Traversal ----");
problem2Instance.PreOrder(BinaryTreeRoot);
Console.WriteLine("\n---- PostOrder Traversal ----");
problem2Instance.PostOrder(BinaryTreeRoot);
*/

/* Problem 1

Problem1 problem1Instance = new();
TreeNode? BinaryTreeRoot = TreeHelper.CreateBinaryTree();
problem1Instance.InOrderTraversalRecursive(BinaryTreeRoot);

 */


Console.WriteLine("\n\n---- End ----\n");