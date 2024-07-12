

using VinitKumar.Problems;
using VinitKumar.Utilities;


Console.WriteLine("Problem 6");

TreeNode? treeNode = new TreeNode(1);
treeNode.Left = new TreeNode(2);
treeNode.Right = new TreeNode(2);
treeNode.Left.Left = new TreeNode(3);
treeNode.Left.Right = new TreeNode(4);
treeNode.Right.Left = new TreeNode(4);
treeNode.Right.Right = new TreeNode(3);
Console.WriteLine($"IsSymmetric tree ? - {Problem6.IsSymmetric(treeNode)}");


Console.WriteLine("Problem 5");

TreeNode? treeNode1 = new TreeNode(1);
treeNode1.Left = new TreeNode(2);
treeNode1.Right = new TreeNode(3);
treeNode1.Left.Left = new TreeNode(4);
treeNode1.Left.Right = new TreeNode(5);
treeNode1.Right.Left = new TreeNode(6);
treeNode1.Right.Right = new TreeNode(7);
TreeNode? treeNode2 = new TreeNode(1);
treeNode2.Left = new TreeNode(2);
treeNode2.Right = new TreeNode(3);
treeNode2.Left.Left = new TreeNode(4);
treeNode2.Left.Right = new TreeNode(5);
treeNode2.Right.Left = new TreeNode(6);
treeNode2.Right.Right = new TreeNode(7);
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