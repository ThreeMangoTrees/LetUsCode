

using VinitKumar.Problems;
using VinitKumar.Utilities;

/* 

Problem 2 

*/

Problem2 problem2Instance = new();
TreeNode? BinaryTreeRoot = TreeHelper.CreateBinaryTree();
Console.WriteLine("\n---- PreOrder Traversal ----");
problem2Instance.PreOrder(BinaryTreeRoot);
Console.WriteLine("\n---- PostOrder Traversal ----");
problem2Instance.PostOrder(BinaryTreeRoot);


/* Problem 1

Problem1 problem1Instance = new();
TreeNode? BinaryTreeRoot = TreeHelper.CreateBinaryTree();
problem1Instance.InOrderTraversalRecursive(BinaryTreeRoot);

 */
